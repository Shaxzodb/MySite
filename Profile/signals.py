from django.dispatch import receiver # add this
from django.db.models.signals import post_save, post_delete
from .models import Profile

@receiver(post_save, sender=Profile) #add this
def profile_save_user(sender, instance, **kwargs):
    user = instance.username
    profile = Profile.objects.get(username=user)
    user.last_name = profile.last_name or ''
    user.first_name = profile.first_name or ''
    user.email = profile.email
    user.phone = profile.phone
    user.save()
    
@receiver(post_delete, sender=Profile) #delete this
def profile_delete_user(sender, instance, **kwargs):
    user = instance.username
    user.delete()
    
    
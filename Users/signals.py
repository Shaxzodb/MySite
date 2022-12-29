from django.dispatch import receiver # add this
import logging
db_logger = logging.getLogger('db')

from django.dispatch import receiver # add this
from django.db.models.signals import post_save, post_delete
from .models import Profile, CustomUserModel

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
    

@receiver(post_save, sender=CustomUserModel) #add this
def user_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            username = instance,
            email = instance.email
        )
    
@receiver(post_save, sender=CustomUserModel)
def user_save_profile(sender, instance, **kwargs):
    # instance.profile.save()
    try:
        Profile.objects.filter(
            username = instance
        ).update(
            last_name = instance.last_name,
            first_name = instance.first_name,
            email = instance.email,
            phone = instance.phone,
        )
    except:
        db_logger.warning(
            f'Foydalanuvchi {instance} - Users Signalda Xatolik o\'zgaritirib bo\'lmadi'
        )
from django.dispatch import receiver # add this
from django.db.models.signals import post_save
from Profile.models import Profile
from .models import CustomUserModel
import logging
db_logger = logging.getLogger('db')

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
from django.dispatch import receiver # add this
import logging
from django.core.mail import send_mail
from django.utils import translation
from middleware.token import account_activation_token
from django.dispatch import receiver # add this
from django.db.models.signals import post_save, post_delete
from django.conf import settings
from .models import Profile, CustomUserModel, Token

db_logger = logging.getLogger('db')
@receiver(post_save, sender=Profile) #add this
def profile_save_user(sender, instance, **kwargs):
    user = instance.user
    profile = Profile.objects.get(user=user)
    user.last_name = profile.last_name or ''
    user.first_name = profile.first_name or ''
    user.email = profile.email
    user.phone = profile.phone
    user.save()
    
@receiver(post_delete, sender=Profile) #delete this
def profile_delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

@receiver(post_save, sender=CustomUserModel) #add this
def user_create_profile(sender, instance, created, **kwargs):
    if created: 
        UserProfile = Profile.objects.create(
            user = instance,
            email = instance.email
        )
        UserToken = Token.objects.create(
            user = instance,
            token = account_activation_token.make_token(instance)
        )
        user_language = translation.get_language()
        send_mail(
            'Email Tastiqlash',
            f'http://127.0.0.1:8000/{user_language}/email-verify/{UserToken.token}/',
            str(settings.EMAIL_HOST_USER),
            [str(UserProfile.email)],
            fail_silently=False,
        )
    
@receiver(post_save, sender=CustomUserModel)
def user_save_profile(sender, instance, **kwargs):
    
    try:
        Profile.objects.filter(
            user = instance
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
from django.dispatch import receiver # add this
import logging
from django.core import mail
from django.utils import translation
from middleware.token import account_activation_token
from django.dispatch import receiver # add this
from django.db.models.signals import post_save, post_delete, pre_save,m2m_changed
from django.conf import settings
from .models import Profile, CustomUserModel, Token, AllSendEmail
from django.contrib.sites.models import Site
from django.template.loader import render_to_string

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
        current_site = Site.objects.get_current()
        try:
            html_message = render_to_string(
                'email/email_verify.html', 
                {
                    'username': UserProfile.user.username,
                    'current_site': current_site,
                    'user_language': user_language,
                    'UserToken': UserToken
                }
            )
            with mail.get_connection() as connection:
                msg = mail.EmailMessage(
                    'Email Tastiqlash',
                    html_message,
                    str(settings.EMAIL_HOST_USER),
                    [str(UserProfile.email)],
                    connection=connection,
                )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
    
        except:
            db_logger.warning(
                f'Foydalanuvchi {instance} - Email Xabar yuborishda Xato ruy berdi'
            )
    
@receiver(post_save, sender = CustomUserModel)
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
        
@receiver(post_save, sender = AllSendEmail)
def send_messages(sender, instance, **kwargs):
        email_list = [email for email, confirm in list(CustomUserModel.objects.values_list("email","confirm")) if confirm ]
        if email_list != []:
            with mail.get_connection() as connection:
                msg = mail.EmailMessage(
                    instance.subject,
                    instance.message,
                    str(settings.EMAIL_HOST_USER),
                    email_list,
                    connection=connection,
                )
                msg.send()
    
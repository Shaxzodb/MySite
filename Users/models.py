from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field
from autoslug import AutoSlugField

# Create your models here.     
class CustomUserModel(AbstractUser):
    phone = PhoneNumberField(
        null = True,
        blank = True
    )
    confirm = models.BooleanField(
        name = 'confirm',
        help_text="Do you agree to send news to your email?",
        default = False
    )
    email_verification = models.BooleanField(
        default = False
    )
    def __str__(self) -> str:
        return str(self.username[:15] + '...') if len(str(self.username)) > 15 else str(self.username)
    
    
    def get_absolute_url(self):
        return reverse('login')

class Token(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete = models.CASCADE 
    )
    token = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return str(self.user.username)
    
class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete = models.CASCADE 
    )
    phone = PhoneNumberField(
        null = True,
        blank = True
    )
    email = models.EmailField(
        null = True,
        blank = True
    )
    user_pic = models.ImageField(
        help_text='User Avatar',
        upload_to = 'profile_pics/',
        blank = True, 
        null  = True
    )
    bio = CKEditor5Field(
        max_length = 500,
        null = True,
        blank = True,
        config_name='extends_profile'
    )
    location = models.CharField(
        max_length = 125, 
        blank = True, 
        null = True
    )
    last_name = models.CharField(
        max_length = 125, 
        blank = True, 
        null = True
    )
    first_name = models.CharField(
        max_length = 125, 
        blank = True, 
        null = True
    )
    website = models.URLField(
        blank = True,
        null = True
    )
    birth_date = models.DateField(
        null = True,
        blank = True
    )
    slug = AutoSlugField(
        populate_from='_username',
        unique = True
    )
    @property
    def _username(self):
        return self.user.username
 
    friends = models.ManyToManyField(
        get_user_model(),
        related_name = 'friends',
        blank = True
    )
    
    def total_friends(self):
        return self.friends.count()
    
    def __str__(self) -> str:
        return str(self._username)
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

class AllSendEmail(models.Model):
    subject = models.CharField(
        'Subject',
        max_length = 256
    )
    message = CKEditor5Field(
        config_name='default'
    )
    def total(self):
        return self.user_email.count()
    def __str__(self) -> str:
        return str(self.subject[:30] + '...') \
            if len(self.subject) > 30 else str(self.subject)
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Profile(models.Model):
    username = models.OneToOneField(
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
    user_image = models.ImageField(
        upload_to = 'profile_pics/',
        blank = True, 
        null  = True
    )
    bio = CKEditor5Field(
        max_length = 500,
        null = True,
        blank = True,
        config_name='extends-profile'
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
    slug = models.SlugField(
        unique=True
    )
    
    def save(self, *args, **kwargs):
        value = self.username.username
        self.slug = slugify(
            value, 
            allow_unicode = True
        )
        super().save(*args, **kwargs)
        
    def __str__(self) :
        return str(self.username)
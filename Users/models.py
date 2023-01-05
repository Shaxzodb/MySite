from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.     
class CustomUserModel(AbstractUser):
    phone = PhoneNumberField(
        null = True,
        blank = True
    )
    email_verification = models.BooleanField(
        default = False
    )
    def __str__(self) -> str:
        return str(self.username)
    
    def get_absolute_url(self):
        return reverse('login')

class Token(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete = models.CASCADE 
    )
    token = models.CharField(max_length=256)
        
    def __str__(self) -> str:
        return str(self.user)
    
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
    slug = models.SlugField(
        unique=True
    )
    friends = models.ManyToManyField(
        get_user_model(),
       related_name = 'friends',
       blank = True
    )
    
    def total_friends(self):
        return self.friends.count()
    
    def save(self, *args, **kwargs):
        value = self.user.username
        self.slug = slugify(
            value, 
            allow_unicode = True
        )
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})
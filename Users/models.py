from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

# Create your models here.

class CustomUserModel(AbstractUser):
    phone = PhoneNumberField(
        null = True,
        blank = True
    )
    # email = models.EmailField(unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    
    
    
    def get_absolute_url(self):
        return reverse('login')
    
    def __str__(self) -> str:
        return str(self.username)

    
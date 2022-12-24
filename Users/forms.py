from .models import CustomUserModel
from django import forms
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class CustomCreateUserForm(UserCreationForm):
    username = None
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["email"].required = True
          # self.fields["phone"].required = True

    class Meta:
        model   = CustomUserModel
        fields  = UserCreationForm.Meta.fields + ('email',)
        widgets = {}

class CustomUpdateUserForm(UserChangeForm):
    class Meta:
        model  = CustomUserModel
        fields = UserChangeForm.Meta.fields
        
        
        

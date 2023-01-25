from .models import CustomUserModel, Profile
from django import forms
from crispy_bootstrap5.bootstrap5 import FloatingField, BS5Accordion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import AccordionGroup
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm


class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True, min_length=6, max_length=35)
    helper = FormHelper()
    helper.layout = Layout(
        FloatingField("username", autocomplete="username"),
        FloatingField("email", autocomplete="email"),
        FloatingField("password1", autocomplete="password1"),
        FloatingField("password2", autocomplete="password2"),
        'confirm'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
        
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('email','confirm')
        widgets = {}
        
class UserLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)
    username = forms.CharField(required=True, min_length=6, max_length=35)
    helper = FormHelper()
    helper.layout = Layout(
        FloatingField("username", autocomplete="username"),
        FloatingField("password", autocomplete="password"),
        'remember_me'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = CustomUserModel
        fields = ['username','password']
        widgets = {}
    

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = UserChangeForm.Meta.fields
        
class ProfileForm(forms.ModelForm):
    
    helper = FormHelper()
    helper.layout = Layout(
        # self.helper.form_tag = False
        # self.helper.include_media = False 
        BS5Accordion(
            AccordionGroup('#1',  
                FloatingField("last_name", autocomplete="last_name"),
                FloatingField("first_name", autocomplete="first_name"),
                'user_pic'
            ),
            AccordionGroup('#2',
                'bio',
            ),
            AccordionGroup('#3',
                FloatingField("location", autocomplete="location"),
                FloatingField("website", autocomplete="website"),
                FloatingField("phone", autocomplete="phone"),
                FloatingField("birth_date", autocomplete="birth_date"),
                
            ),
            flush=True,
            # always_open=True
        )
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    class Meta:
        model = Profile
        fields = ['bio','last_name','first_name','location','website','phone','user_pic',"birth_date"]
        widgets = {}
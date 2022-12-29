from .models import CustomUserModel
from django import forms
from crispy_bootstrap5.bootstrap5 import FloatingField, BS5Accordion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Accordion, AccordionGroup
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomCreateUserForm(UserCreationForm):
    helper = FormHelper()
    helper.layout = Layout(
        # self.helper.form_tag = False
        # self.helper.include_media = False 
        BS5Accordion(
            AccordionGroup('username and email',
                FloatingField("username", autocomplete="username"),
                FloatingField("email", autocomplete="email"),
            ),
            AccordionGroup('password',
                FloatingField("password1", autocomplete="password1"),
                FloatingField("password2", autocomplete="password2"),
            ),
            flush=True,
            always_open=True
        )
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
        
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('email',)
        widgets = {}

class CustomUpdateUserForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = UserChangeForm.Meta.fields
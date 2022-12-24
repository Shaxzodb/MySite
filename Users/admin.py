from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel
from .forms import CustomCreateUserForm, CustomUpdateUserForm
# Register your models here.


@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    add_form      = CustomCreateUserForm
    form          = CustomUpdateUserForm
    model         = CustomUserModel 
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                'fields' : (
                    'phone',
                    'email',
                )
            }
        ),
    )
    fieldsets    = UserAdmin.fieldsets + (
        (
            None,
            {
                'fields' : (
                    'phone',
                )
            }
        ),
    )
    list_display    = ['username','email','phone','is_staff']
    list_filter     = ['is_active','is_staff','is_superuser']
    search_fields   = ['username','email','phone','last_name','first_name']
    ordering        = ['-username']

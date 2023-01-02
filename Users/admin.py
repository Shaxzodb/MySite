from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel, Profile, Token
from .forms import CustomCreateUserForm, CustomUpdateUserForm
# Register your models here.
@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    add_form = CustomCreateUserForm
    form = CustomUpdateUserForm
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
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                'fields' : (
                    'phone',
                    'email_verification',
                )
            }
        ),
    )
    list_display = ['username','email','phone','is_staff']
    list_filter = ['is_active','is_staff','is_superuser']
    search_fields = ['username','email','phone','last_name','first_name']
    ordering = ['-username']
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','email','phone','last_name','first_name']
    
admin.site.register(Token)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel, Profile, Token, AllSendEmail
from .forms import  UserCreateForm, UserUpdateForm
from django.utils.html import format_html
from django.contrib.sites.models import Site

# Register your models here.
@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserUpdateForm
    
    def thumb(self, obj):
        current_site = Site.objects.get_current()
        if not not obj.profile.user_pic:
            return format_html(f"<img src='http://{current_site}/media/{str(obj.profile.user_pic)}' style='border-radius:100%'  width='35' height='35' />")
        return format_html("<img src='http://{}/static/img/user_default_pic.png' style='border-radius:100%'  width='35' height='35' />".format(current_site))

    thumb.allow_tags = True
    thumb.__name__ = 'Thumb'
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Addition',
            {
                'fields' : (
                    'phone',
                    'email',
                    'confirm'
                )
            }
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            'Addition',
            {
                'fields' : (
                    'phone',
                    'email_verification',
                    'confirm'
                )
            }
        ),
    )
    jazzmin_section_order = ('Addition',)
    list_display = ['thumb','username','phone','is_staff','confirm','email_verification']
    list_filter = ['is_active','is_staff','is_superuser','confirm','email_verification']
   
    search_fields = ['username','email','phone','last_name','first_name']
    ordering = ['-username']
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def thumb(self, obj):
        current_site = Site.objects.get_current()
        if not not obj.user_pic:
            return format_html(f"<img src='http://{current_site}/media/{str(obj.user_pic)}' style='border-radius:100%'  width='35' height='35' />")
        return format_html("<img src='http://{}/static/img/user_default_pic.png' style='border-radius:100%'  width='35' height='35' />".format(current_site))

    thumb.allow_tags = True
    thumb.__name__ = 'Thumb'
    ordering = ['-user__last_login']
    list_display = ['thumb','user','email','phone','last_name','first_name']
    
admin.site.register(Token)

@admin.register(AllSendEmail)
class SomeModelAdmin(admin.ModelAdmin):
    pass
    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['show_save_and_continue'] = False
    #     extra_context['show_save_and_add_another'] = False
    #     return super(SomeModelAdmin,self).changeform_view(request, object_id, extra_context=extra_context)

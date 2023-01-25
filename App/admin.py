from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from Articles.models import ArticleModel

# Register your models here.

admin.site.index_title = _('Admin Panel')
admin.site.site_header  = _('OKIAN.UZ')
admin.site.site_title = _('OKIAN.UZ')

# class AdminSite(admin.AdminSite):
#     index_title = _('Admin Panel')
#     site_header = _('OKIAN.UZ')
#     site_title = _('OKIAN-UZ')
    
# admin_site = AdminSite(name='admin_site_panel')
# admin_site.register(ArticleModel)





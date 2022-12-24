from django.contrib import admin
from .models import HtmlCode, ScriptCode
# Register your models here.

@admin.register(HtmlCode, ScriptCode)
class HtmlAdmin(admin.ModelAdmin):
    list_display = ['id','name']

from django.contrib import admin
from .models import HEADCode, BODYCode
# Register your models here.

@admin.register(HEADCode, BODYCode)
class CodeAdmin(admin.ModelAdmin):
    list_display = ['name','info']

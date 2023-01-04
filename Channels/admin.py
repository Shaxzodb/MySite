from django.contrib import admin
from .models import Channel, Post

# Register your models here.
admin.register(Channel)
class AdminChannel(admin.ModelAdmin):
    list_display = ['slug','name','owner','total_subscribers']

admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['author','channel']
    
admin.site.register(Post, AdminPost)
admin.site.register(Channel, AdminChannel)

from django.contrib import admin
from .models import Channel, Post

# Register your models here.
class PostInlines(admin.StackedInline):
    model = Post
    ordering = ['-created_pt']
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author','channel']
    
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    ordering = ['-created_ch']
    inlines = [PostInlines]
    list_display = ['slug', 'name', 'owner', 'total_subscribers']

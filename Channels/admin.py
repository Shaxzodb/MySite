from django.contrib import admin
from .models import Channel, Post
from django.utils.html import format_html

#Register your models here.
class PostInlines(admin.StackedInline):
    model = Post
    ordering = ['-created_pt']
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author','channel']
    

@admin.display(description="Images")
def Avatar(obj):
    if not obj.image_ch:
        return format_html(
            f"<div style='width:30px;margin:0;color:#fff;padding:0;height:30px'><center><p style='background-color:blue; width:30px;margin:0;color:#fff;padding:0;height:30px;color:fff !important;border-radius:50%'>{obj.name[0]}</p></center></div>"
        )
    return format_html(f"<img src='{str(obj.image_ch.url)}' style='border-radius:100%'  width='30' height='30' />")
    

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    ordering = ['-created_ch']
    inlines = [PostInlines]
    list_per_page = 15
    fieldsets = (
        ("General", 
            {
                "fields": (
                    'name',
                    'owner',
                    'image_ch',
                    'description',
                    'created_ch',
                    'updated_ch',
                ),
            }
        ),
        ("Admins", 
            {
                "fields": (
                    'admins',
                ),
            }
        ),
        ("Subscribers", 
            {
                "fields": (
                    'subscribers',
                ),
            }
        ),
    )
    list_display = [Avatar,'slug', 'name', 'owner', 'total_subscribers']
    readonly_fields = ['created_ch','updated_ch',"subscribers",]
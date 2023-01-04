from django.contrib import admin
from .models import ArticleModel
from django.utils.html import format_html
from Comments.admin import Comments
# Register your models here.

@admin.display(description="Created Date | Updated Date")
def create_updated(obj):
        return format_html(
            "<strong style='color:black'>CR - {} <br/><hr/> <span style='color:red'>UD - {}</span></strong>",
            obj.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        )
        
@admin.display(description="Title")
def title(obj):
    if len(obj.title_at)>=35:
        return format_html(
            '<strong style="color:blue">{}</span></strong>',
            obj.title_at[:35] + '...'     
        )
    else:
        return format_html(
           '<strong style="color:black">{}</span></strong>',
            obj.title_at,
        )

@admin.register(ArticleModel)
class ArticlesAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    inlines = [Comments]
    list_display = ['id', title,create_updated]
    add_fieldsets = (
        (None, {
            "fields": (
                'title_at',
                'author',
                'content_at',
                'image_at',
            ),
        }),
    )
    fieldsets = (
        (None, {
            "fields": (
                'title_at',
                'author',
                'content_at',
                'image_at',
                'likes',
                'dislikes'
            ),
        }),
    )
    ordering = ['-updated_at']
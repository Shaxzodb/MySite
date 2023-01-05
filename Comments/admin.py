from django.contrib import admin
from .models import ArticleComment
from django.utils.html import format_html
# Register your models here.

@admin.display(description="Created Date | Updated Date")
def create_updated(obj):
        return format_html(
            "<strong style='color:black'>CR - {} <br/><hr/> <span style='color:red'>UD - {}</span></strong>",
            obj.created_cm.strftime('%Y-%m-%d %H:%M:%S'),
            obj.updated_cm.strftime('%Y-%m-%d %H:%M:%S')
        )
        
@admin.register(ArticleComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author',create_updated]
    ordering = ['-updated_cm']

class CommentsInline(admin.StackedInline):
    model = ArticleComment
    ordering = ['-created_cm']
    extra = 0

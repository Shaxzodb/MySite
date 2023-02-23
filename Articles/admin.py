from django.contrib import admin
from .models import ArticleModel
from django.utils.html import format_html
from Comments.admin import CommentsInline
from django.templatetags.static import static

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
    # Render filtered options only after 5 characters were entered
    filter_input_length = {
        "author": 5,
    }
    inlines = [CommentsInline]
    list_display = ['id','author', title, create_updated]
    
    fieldsets = (
        ("General", {
            "fields": (
                'title_at',
                'headshot_image',
                'image_at',
                'author',
                'content_at',
            ),
        }),
        (
            'Addition',
            {
                'fields' : (
                    'likes',
                    'dislikes',
                )
            }
        ),
    )
    ordering = ['-updated_at']
    list_per_page = 15
    
    readonly_fields = ["headshot_image","likes","dislikes"]
    
    def headshot_image(self, obj):
        if not obj.image_at:
            return format_html("<img src='{url}'  width='300px'/>".format(url = static('img/908418-200.png')))
        return format_html("<img src='{url}'  width='300px'/>".format(url = obj.image_at.url)
    )
        
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)
    
    # exclude = ['author',]
from django.db import models
from django.contrib.auth import get_user_model
from Articles.models import ArticleModel
# Create your models here.

class ArticleComment(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )
    
    article_cm = models.ForeignKey(
        ArticleModel,
        on_delete = models.CASCADE,
        related_name = 'comments'
    )
    
    content_cm = models.TextField(
        max_length = 256
    )
    
    created_cm = models.DateTimeField(
        auto_now_add = True
    )
    
    updated_cm = models.DateTimeField(
        auto_now = True
    )
    
    is_check = models.BooleanField(
        default = True
    )
    
    
    def __str__(self):
        return str(self.article_cm.title_at[:30] + '...') \
            if len(self.article_cm.title_at) > 30 else str(self.article_cm.title_at)

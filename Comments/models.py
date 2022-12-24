from django.db import models
from django.contrib.auth import get_user_model
from Articles.models import ArticleModel
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class CommentArticle(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )
    
    article_comment = models.ForeignKey(
        ArticleModel,
        on_delete = models.CASCADE,
        related_name = 'article_comments'
    )
    
    comment = CKEditor5Field(
        max_length = 256,
        config_name='extends_comment'
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
    
    # likes = models.ManyToManyField(
    #     get_user_model(),
    #     related_name = 'comment_likes'
    # )
    
    def __str__(self):
        return (self.comment[:30] + '...') if len(self.comment) > 30 else self.comment
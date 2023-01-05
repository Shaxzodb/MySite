from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field
from .validate import validate_length
from django.urls import reverse
from middleware.token import account_activation_token
# Create your models here.
class Channel(models.Model):
    name = models.CharField(
        validators=[validate_length],
        max_length=256,
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    subscribers = models.ManyToManyField(
        get_user_model(),
        blank = True,
        related_name='subscription'
    )
    slug = models.SlugField(
        'username',
        max_length = 50,
        validators = [validate_length],
        blank = True
    )
    
    created_ch = models.DateTimeField(
        auto_now_add = True
    )
    updated_ch = models.DateTimeField(
        auto_now = True
    )
    
    def total_subscribers(self):
        return self.subscribers.count()
    
    def __str__(self) -> str:
        return str(self.slug[:35] + '...') if len(str(self.slug)) > 35 else str(self.slug)
    
    def get_absolute_url(self):
        return reverse("channel", kwargs={"slug": self.slug})

class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    channel = models.ForeignKey(
        'Channel',
        on_delete=models.CASCADE,
        related_name='post'
    )
    content_pt = CKEditor5Field(
        config_name='extends_article'
    )
    likes = models.ManyToManyField(
        get_user_model(),
        blank = True,
        related_name='likes_pt'
    )
    dislikes = models.ManyToManyField(
        get_user_model(),
        blank = True,
        related_name='dislikes_pt'
    )
    created_pt = models.DateTimeField(
        auto_now_add = True
    )
    updated_pt = models.DateTimeField(
        auto_now = True
    )
    def total_likes(self):
        return self.likes.count()
    
    def total_dislikes(self):
        return self.dislikes.count()
    
    def __str__(self) -> str:
        return str(self.author[:35] + '...') if len(str(self.author)) > 35 else str(self.author)
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth import get_user_model
from hitcount.models import HitCount, HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from autoslug import AutoSlugField

# Create your models here.

class ArticleModel(models.Model, HitCountMixin):
    author = models.ForeignKey(
        get_user_model(),
        null = True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name = 'article'
    )
    title_at = models.CharField(
        max_length = 256
    )
    image_at = models.ImageField(
        upload_to = 'articles_images/', 
        null =True,
        blank = True
    )
    content_at = CKEditor5Field(
        config_name='default'
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True,
    )
    slug = AutoSlugField(
        populate_from='title_at',
        unique = True
    )
    is_check = models.BooleanField(
        default = True
    )
    likes = models.ManyToManyField(
        get_user_model(),
        blank = True,
        related_name = 'likes'
    )
    dislikes = models.ManyToManyField(
        get_user_model(),
        blank = True,
        related_name = 'dislikes'
    )
    hit_count_generic = GenericRelation(
        
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    changed = models.BooleanField(default=False)
    def total_likes(self):
        return self.likes.count()
    
    def total_dislikes(self):
        return self.dislikes.count()
    
    def __str__(self) -> str:
        return str(self.title_at[:50] + '...') if len(self.title_at) > 50 else str(self.title_at)
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
    
    
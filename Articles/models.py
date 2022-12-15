from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
# here is an example model with a GenericRelation
# Create your models here.
class ArticleModel(models.Model, HitCountMixin):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    title = models.CharField(
        max_length = 256
    )
    
    image = models.ImageField(
        upload_to = 'articles_images/', 
        null =True,
        blank = True
    )
    
    content = CKEditor5Field(
        config_name='extends_article'
    )
    
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    
    updated_at = models.DateTimeField(
        auto_now = True
    )
    
    slug = models.SlugField(
        max_length=256,
        null = True,
        blank = True,
        unique = True
    )
    
    is_check = models.BooleanField(
        default = True
    )
    
    likes = models.ManyToManyField(
        get_user_model(),
        blank = True,
        related_name='article_likes'
    )
    
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    def save(self, *args, **kwargs):
        self.slug = slugify(
            str(self.title),
            allow_unicode = True
        )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return (self.title[:35] + '...') if len(self.title) > 35 else self.title
    
    
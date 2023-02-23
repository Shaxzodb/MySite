from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field
from .validate import validate_length
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.

class CPTModel(models.Model):
    created = models.DateTimeField(
        auto_now_add = True
    )
    updated = models.DateTimeField(
        auto_now = True
    )
    class Meta:
        abstract = True
        
class Channel(CPTModel):
    name = models.CharField(
        validators=[validate_length],
        max_length=256,
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name ='owner'
    )
    image_ch = models.ImageField(
        'channel image',
        upload_to = 'channel_images/', 
        blank = True,
        null = True
    )
    admins = models.ManyToManyField(
        get_user_model(),
        blank = True,
        related_name='admins'
    )
    subscribers = models.ManyToManyField(
        get_user_model(),
        blank = True,
        related_name='subscription'
    )
    slug = models.SlugField(
        'username',
        max_length = 50,
        unique = True,
        blank= True,
        validators = [validate_length],
    )
    
    description = models.TextField(
        blank=True,
        null=True,
        max_length=256
    )
    def total_subscribers(self):
        return self.subscribers.count()
    
    def total_admins(self):
        return self.admins.count()
    
    def __str__(self) -> str:
        return str(self.name[:30] + '...') if len(str(self.name)) > 30 else str(self.name)
    
    def get_absolute_url(self):
        return reverse("channel", kwargs={"slug": self.slug})
 
class Post(CPTModel):
    
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    channel = models.ForeignKey(
        'Channel',
        on_delete=models.CASCADE,
        related_name='post'
    )
    changed = models.BooleanField(default=False)
    content = CKEditor5Field(
        config_name='default',
   
    )
    


    def __str__(self) -> str:
        return str(self.author[:35] + '...') if len(str(self.author)) > 35 else str(self.author)
    
    # def clean(self):
    #     super().clean()
    #     if self.quiz_mode == True:
    #         raise ValidationError('Qiymat mavjud emas')
    # def save(self, *args, **kwargs):
    #     if self.question != '':
    #         self.quiz_mode = True
    #     super(Post, self).save(*args, **kwargs)
        
    
    
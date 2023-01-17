from django.dispatch import receiver # add this
from django.db.models.signals import pre_save
from .models import Channel
from django.utils.text import slugify
import uuid

@receiver(pre_save, sender=Channel) #add this
def user_create_profile(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            str(uuid.uuid4()),
            allow_unicode = True
        )
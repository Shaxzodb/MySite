from django.db import models
# Create your models here.

class HEADCode(models.Model):
    name = models.CharField(
        max_length = 256
    )
    info = models.CharField(
        max_length = 256,
        blank = True,
        null = True
    )
    code = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class BODYCode(models.Model):
    name = models.CharField(
        max_length = 256
    )
    info = models.CharField(
        max_length = 256,
        blank = True,
        null = True
    )
    code = models.TextField()

    def __str__(self) -> str:
        return self.name





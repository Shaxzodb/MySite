from django.db import models
# Create your models here.

class HtmlCode(models.Model):
    
    name = models.CharField(
        max_length = 256
    )
    
    html_code = models.TextField()

    def __str__(self):
        return self.name
    
class ScriptCode(models.Model):
    
    name = models.CharField(
        max_length = 256
    )
    
    script_code = models.TextField()

    def __str__(self):
        return self.name





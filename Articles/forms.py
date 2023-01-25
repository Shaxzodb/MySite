from django import forms
from .models import ArticleModel

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title_at','image_at','content_at']
        widgets = {}
        


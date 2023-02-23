from django import forms
from .models import ArticleModel

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title_at','content_at','image_at']
        widgets = {
            'title_at':forms.TextInput(attrs={'placeholder':'Article Title','style':'border:none !important;','class':'shadow-none mb-3 p-0'}),
            'image_at':forms.FileInput(attrs={'style':'border:none !important;','class':'shadow-none'})
        }
        


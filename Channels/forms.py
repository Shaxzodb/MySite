from django import forms
from .models import Channel, Post

class ChannelCreateForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['name','image_ch','description','slug']

class ChannelEditFrom(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['name','image_ch','description','slug']
        
class PostCreateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['content']
        
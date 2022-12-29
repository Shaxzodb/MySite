from django.shortcuts import render
from django.views.generic import ListView
from hitcount.views import HitCountDetailView
from .models import ArticleModel
from django.utils import translation
from django.conf import settings

# Create your views here.
class ArticleListView(ListView):
    model = ArticleModel
    template_name = 'article_list.html'
    
class ArticleDetailView(HitCountDetailView):
    model = ArticleModel
    template_name: str = 'article_detail.html'
    count_hit = True

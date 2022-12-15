from django.shortcuts import render
from django.views.generic import ListView, DetailView
from hitcount.views import HitCountDetailView, HitCountMixin
from .models import ArticleModel
from django.views.generic.dates import ArchiveIndexView
from django.http import Http404
# Create your views here.

class ArticleListView(ListView):
    model = ArticleModel
    template_name = 'article_list.html'
    
    
class ArticleDetailView(HitCountDetailView):
    model = ArticleModel
    template_name: str = 'article_detail.html'
    count_hit = True
    # def get_queryset(self):
    #     try:
    #         return ArticleModel.objects.filter(
    #             slug = self.kwargs['slug'],
    #         )
    #     except:
    #         raise Http404
    # queryset = ArticleModel.objects.all()
    # date_field = "created_at"
    # make_object_list = True
    # allow_future = True



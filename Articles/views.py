from django.views.generic import ListView
from hitcount.views import HitCountDetailView
from .models import ArticleModel
from django.shortcuts import get_object_or_404
# from django.http import Http404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

class ArticleListView(ListView):
    model = ArticleModel
    template_name = 'articles/article_list.html'

    def get_queryset(self):
        qs =  super().get_queryset()
        return qs.all().order_by('likes', 'hit_count_generic', '-dislikes', 'created_at')

class ArticleDetailView(HitCountDetailView):
    model = ArticleModel
    template_name: str = 'articles/article_detail.html'
    count_hit = True
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(
            ArticleModel, 
            slug = self.kwargs['slug']
        )
        article = get_object_or_404(ArticleModel, slug = self.kwargs['slug'])
        confirmed_likes = article.likes.filter(id=self.request.user.id).exists()
        confirmed_dislikes = article.dislikes.filter(id=self.request.user.id).exists()
        context["confirmed_likes"] = confirmed_likes
        context["confirmed_dislikes"] = confirmed_dislikes
        total_likes = stuff.total_likes()
        total_dislikes = stuff.total_dislikes()
        context["likes"] = total_likes
        context["dislikes"] = total_dislikes
        
        return context


@login_required()
def LikesView(request, slug):
    if request.method == 'POST':
        article = get_object_or_404(ArticleModel, slug = slug)
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)
            if article.dislikes.filter(id=request.user.id).exists():
                article.dislikes.remove(request.user)
            article.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(slug)]))

@login_required()
def UnLikesView(request, slug):
    if request.method == 'POST':
        article = get_object_or_404(ArticleModel, slug = slug)
        if article.dislikes.filter(id=request.user.id).exists():
            article.dislikes.remove(request.user)
        else:
            if article.likes.filter(id=request.user.id).exists():
                article.likes.remove(request.user)
            article.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(slug)]))  
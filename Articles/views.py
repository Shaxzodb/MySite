from django.views.generic import CreateView, UpdateView, ListView
from hitcount.views import HitCountDetailView
from .models import ArticleModel
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from middleware.language import LocaleMiddleware
from Users.models import CustomUserModel
from .filters import ArticleFilter
from django.db.models import Max, Min

# Create your views here.

class article_list(ListView):
    template_name = 'article/article_page.html'
    model = ArticleModel
    #context_object_name = 'filter'
    def get_queryset(self):
        return ArticleFilter(
                self.request.GET, 
                queryset=super().get_queryset().all().select_related('author').annotate(max_likes=Max('likes'),
                min_dislikes=Min('dislikes')).order_by('hit_count_generic','-max_likes','min_dislikes','-created_at')
            ).qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter(
                self.request.GET, 
                queryset=super().get_queryset().all().select_related('author').annotate(max_likes=Max('likes'),
                min_dislikes=Min('dislikes')).order_by('hit_count_generic','-max_likes','min_dislikes','-created_at')
            )
        return context
    

    
class ArticleDetailView(HitCountDetailView):
    model = ArticleModel
    template_name: str = 'article/article_detail.html'
    count_hit = True
    
    def get_queryset(self):
        return super().get_queryset().select_related('author')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(
            ArticleModel, 
            slug = self.kwargs['slug']
        )
       
        confirmed_likes = stuff.likes.filter(id=self.request.user.id).exists()
        confirmed_dislikes = stuff.dislikes.filter(id=self.request.user.id).exists()
        context["confirmed_likes"] = confirmed_likes
        context["confirmed_dislikes"] = confirmed_dislikes
        total_likes = stuff.total_likes()
        total_dislikes = stuff.total_dislikes()
        context["likes"] = total_likes
        context["dislikes"] = total_dislikes
        return context

@login_required()
def likes_article(request, slug):
    if request.method == 'POST':
        article = get_object_or_404(ArticleModel, slug = slug)
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            if article.dislikes.filter(id=request.user.id).exists():
                article.dislikes.remove(request.user)
            article.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('article_detail', args=[str(slug)]))

@login_required()
def dislikes_article(request, slug):
    if request.method == 'POST':
        article = get_object_or_404(ArticleModel, slug = slug)
        if article.dislikes.filter(id=request.user.id).exists():
            article.dislikes.remove(request.user)
        else:
            if article.likes.filter(id=request.user.id).exists():
                article.likes.remove(request.user)
            article.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(slug)]))

class ArticleCreate(LoginRequiredMixin,CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleForm
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    
class ArticleEdit(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = ArticleModel
    form_class = ArticleForm
    #fields = ['title_at','image_at','content_at']
    template_name = 'article/article_edit.html'
    # form_class = ArticleForm
    def post(self, *args, **kwargs):
        
        
        article = ArticleModel.objects.filter(slug=kwargs['slug'])
        if not article[0].changed:
            article.update(changed=True)
        return super().post(self)
    def test_func(self):
        return self.get_object().author == self.request.user
    
@login_required() 
def article_delete(request, slug):
    if request.method == 'POST':
        article = get_object_or_404(ArticleModel, slug=slug)
        if request.user.id == article.author.id:
            article.delete()
    return redirect('profile', request.user.profile.slug)


''' from django.forms import ModelForm
>>> from myapp.models import Article

# Create the form class.
>>> class ArticleForm(ModelForm):
...     class Meta:
...         model = Article
...         fields = ["pub_date", "headline", "content", "reporter"]
...

# Creating a form to add an article.
>>> form = ArticleForm()

# Creating a form to change an existing article.
>>> article = Article.objects.get(pk=1)
>>> form = ArticleForm(instance=article)
'''

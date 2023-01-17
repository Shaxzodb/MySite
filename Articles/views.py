from django.views.generic import CreateView, UpdateView
from hitcount.views import HitCountDetailView
from .models import ArticleModel
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min
from .forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from middleware.language import LocaleMiddleware
from Users.models import CustomUserModel
# Create your views here.
@LocaleMiddleware
def article_list(request):
    template_name = 'article/article_page.html'
    qs = ArticleModel.objects.all()
    qs.annotate(max_likes=Max('likes'),min_dislikes=Min('dislikes')).order_by('hit_count_generic','-max_likes','min_dislikes','-created_at').values()
    user = get_object_or_404(CustomUserModel, id = request.user.id)
    email_verification = user.email_verification
    return render(request, template_name ,{'email_verification':email_verification,'object_list': qs})
    
class ArticleDetailView(HitCountDetailView):
    model = ArticleModel
    template_name: str = 'article/article_detail.html'
    count_hit = True
    
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
def LikesView(request, slug):
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
def DisLikesView(request, slug):
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
    template_name = 'article/article_edit.html'
    form_class = ArticleForm
    
    def test_func(self):
        return self.get_object().author.id == self.request.user.id
    
@login_required() 
def article_delete(request, slug):
    if request.method == 'POST':
        article = get_object_or_404(ArticleModel, slug=slug)
        if request.user.id == article.author.id:
            article.delete()
    return redirect('profile', request.user.profile.slug)
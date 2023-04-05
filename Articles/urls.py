from django.urls import path
from .views import article_list, ArticleDetailView,\
    ArticleCreate, ArticleEdit, article_delete, likes_article, dislikes_article
from django_ratelimit.decorators import ratelimit
from .feeds import LatestNewsFeed
urlpatterns = [
    path(
        'articles/', 
        ratelimit(
            key = 'ip',
            method = 'GET',
            rate ='50/5m'
        )   
        (article_list.as_view()),
        name = 'article_list'
    ),
    path(
        'article/<slug:slug>/', 
        ratelimit(
            key = 'ip', 
            method = 'GET',
            rate ='50/5m'
        )
        (ArticleDetailView.as_view()),
        name = 'article_detail'
    ),
    path('likes/<slug:slug>', likes_article, name ='likes'),
    path('dislikes/<slug:slug>', dislikes_article, name ='dislikes'),
    path('feed', LatestNewsFeed(), name ='feed'),
    path(
        'create-article/', 
        ratelimit(
            key = 'ip', 
            method = ['GET','POST'],
            rate ='50/5m'
        )
        (ArticleCreate.as_view()),
        name = 'article_create'
    ),
    path(
        'edit-article/<slug:slug>', 
        ratelimit(
            key = 'ip', 
            method = ['GET','POST','PUT','PATCH'],
            rate ='50/5m'
        )
        (ArticleEdit.as_view()),
        name = 'article_edit'
    ),
    path(
        'article-delete/<slug:slug>/', 
        ratelimit(
            key = 'ip', 
            method = 'POST',
            rate ='2/5m'
        )
        (article_delete),
        name = 'article_delete'
    ),
]

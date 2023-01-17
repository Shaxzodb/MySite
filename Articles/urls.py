from django.urls import path
from .views import article_list, ArticleDetailView,\
    LikesView, DisLikesView, ArticleCreate, ArticleEdit, article_delete
from django_ratelimit.decorators import ratelimit

urlpatterns = [
    path(
        'list/', 
        ratelimit(
            key = 'ip',
            method = 'GET',
            rate ='50/5m'
        )   
        (article_list),
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
    path('likes/<slug:slug>', LikesView, name ='likes'),
    path('dislikes/<slug:slug>', DisLikesView, name ='dislikes'),
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

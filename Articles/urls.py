from django.urls import path
from .views import ArticleListView, ArticleDetailView,\
    LikesView, UnLikesView
from django_ratelimit.decorators import ratelimit

urlpatterns = [
    path('list/', 
        ratelimit(
            key = 'ip',
            method = 'GET',
            rate ='100/5m'
        )   
        (ArticleListView.as_view()),
        name = 'list'
    ),
    path('news/<slug:slug>/', 
        ratelimit(
            key = 'ip', 
            method = 'GET',
            rate ='100/5m'
        )
        (ArticleDetailView.as_view()),
        name = 'article_detail'
    ),
    path('likes/<slug:slug>', LikesView, name ='likes'),
    path('dislikes/<slug:slug>', UnLikesView, name ='dislikes')
]

from django.urls import path
from .views import ArticleListView, ArticleDetailView
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
    path('news/<slug:slug>', 
        ratelimit(
            key = 'ip', 
            method = 'GET',
            rate ='100/5m'
        )
        (ArticleDetailView.as_view()),
        name = 'article_detail'
    ),
]

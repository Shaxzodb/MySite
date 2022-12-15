from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('list/', ArticleListView.as_view() ,name = 'list'),
    path('news/<slug:slug>', ArticleDetailView.as_view(),name = 'detail')
]

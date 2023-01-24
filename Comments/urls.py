from django.urls import path
from .views import created_comment, like_and_unlike_comment

urlpatterns = [
    path('comment/<slug:slug>/', created_comment, name = 'comment'),
    path('like-and-unlike-comment/<int:pk>/<slug:article>/', like_and_unlike_comment, name = 'like_and_unlike_comment'),
    
]

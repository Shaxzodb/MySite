from django.urls import path
from .views import created_comment

urlpatterns = [
    path('comment/<slug:slug>/', created_comment, name = 'comment')
]

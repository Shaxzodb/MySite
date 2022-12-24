from django.urls import path
from .views import Base

urlpatterns = [
    path('',Base,name='base')
]

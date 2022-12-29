from django.urls import path
from .views import Homepage, Ratelimited

urlpatterns = [
    path('', Homepage, name='homepage'),
    path('ratelimited/', Ratelimited)
]

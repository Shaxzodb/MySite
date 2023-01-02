from django.urls import path
from .views import Homepage, ratelimited
from django_ratelimit.decorators import ratelimit

urlpatterns = [
    path('', ratelimit(key='ip', rate='100/5m')(Homepage.as_view()), name='homepage'),
    path('ratelimited/', ratelimited)
]

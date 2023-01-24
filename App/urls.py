from django.urls import path
from .views import base, about, rate_limited
from django_ratelimit.decorators import ratelimit

urlpatterns = [
    path('', ratelimit(key='ip', rate='100/5m')(base), name='base'),
    path('about/', ratelimit(key='ip', rate='100/5m')(about), name='about'),
    path('ratelimited/', rate_limited)
]

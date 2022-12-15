from django.urls import path
from .views import CreateUserView, CustomLoginView
from django_ratelimit.decorators import ratelimit
urlpatterns = [
    path('registration/signup', ratelimit(key='ip', method='GET', rate='3/m')(CreateUserView.as_view()), name = 'signup'),
    path('registration/login', CustomLoginView.as_view(), name = 'login')
]

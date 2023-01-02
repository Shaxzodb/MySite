from django.urls import path
from .views import CreateUserView, CustomLoginView, email_verify
from django_ratelimit.decorators import ratelimit
urlpatterns = [
    path('registration/signup/',
        ratelimit(
            key = 'ip', 
            method = 'POST',
            rate ='10/5m'
        )
        (CreateUserView.as_view()), 
        name = 'signup'
    ),
    path('email-verify/<slug:slug>/', email_verify, name = 'email_verify'),
    path('registration/login/', CustomLoginView.as_view(), name = 'login')
]

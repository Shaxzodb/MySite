from django.urls import path
from .views import CreateUserView, CustomLoginView,\
    ProfileView, ProfileUpdateView, email_verify
from django_ratelimit.decorators import ratelimit
urlpatterns = [
    path('register/signup/',
        ratelimit(
            key = 'ip', 
            method = 'POST',
            rate ='10/5m'
        )
        (CreateUserView.as_view()), 
        name = 'signup'
    ),
    path('register/email-verify/<slug:slug>/', email_verify, name = 'email_verify'),
    path('register/login/', CustomLoginView.as_view(), name = 'login'),
    path('profile/<slug:slug>/', ProfileView.as_view(), name = 'profile'),
    path('profile-edit/<slug:slug>/', ProfileUpdateView.as_view(), name = 'profile_edit')
]
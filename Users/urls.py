from django.urls import path
from .views import CreateUserView, CustomLoginView

urlpatterns = [
    path('registration/signup/', CreateUserView.as_view(), name = 'signup'),
    path('registration/login/', CustomLoginView.as_view(), name = 'login')
]

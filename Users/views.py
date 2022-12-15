from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CustomCreateUserForm
from .models import CustomUserModel
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
# Create your views here.

@method_decorator(ratelimit(key='ip', rate='10/m', method='POST'), name='post')
class CreateUserView(CreateView):
    model         = CustomUserModel
    form_class    = CustomCreateUserForm
    template_name = 'registration/signup.html'
    success_url   = 'login'

    def get(self,*args, **kwargs):  
        if self.request.user.is_authenticated:
            return redirect('base')
        else:
            return super().get(self, *args, **kwargs)

@method_decorator(ratelimit(key='post:username', rate='30/m', method='POST'), name='post')
class CustomLoginView(LoginView):
    
    model         = CustomUserModel
    fields        = ('phone','password',)
    template_name = 'registration/login.html'
    success_url   = 'base'
    
    def get(self,*args, **kwargs): 
        if self.request.user.is_authenticated:
            return redirect('base')
        else:
            return super().get(self, *args, **kwargs)



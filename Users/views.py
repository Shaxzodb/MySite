from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CustomCreateUserForm
from .models import CustomUserModel
from django.shortcuts import redirect

# Create your views here.
class CreateUserView(CreateView):
    model = CustomUserModel
    form_class = CustomCreateUserForm
    template_name: str = 'registration/signup.html'
    # success_url = 'login'

    def get(self,*args, **kwargs):  
        if self.request.user.is_authenticated:
            return redirect('homepage')
        else:
            return super().get(self, *args, **kwargs)
        
class CustomLoginView(LoginView):
    model = CustomUserModel
    fields = ('phone','password',)
    template_name: str = 'registration/login.html'
    # success_url = 'homepage'
    
    def get(self,*args, **kwargs):  
        if self.request.user.is_authenticated:
            return redirect('homepage')
        else:
            return super().get(self, *args, **kwargs)
            
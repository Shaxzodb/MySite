from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CustomCreateUserForm
from .models import CustomUserModel, Token
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
class CreateUserView(CreateView):
    model = CustomUserModel
    form_class = CustomCreateUserForm
    template_name: str = 'registration/signup.html'

    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('homepage')
        else:
            return super().get(self, *args, **kwargs)
        
class CustomLoginView(LoginView):
    model = CustomUserModel
    fields = ('phone','password',)
    template_name: str = 'registration/login.html'
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('homepage')
        else:
            return super().get(self, *args, **kwargs)

def email_verify(request, slug):
    token = get_object_or_404(Token, token = slug)
    CustomUserModel.objects.filter(
        id = token.user.id
    ).update(
        email_verification = True
    )
    messages.success(request,'Emailingiz Tastiqlandi')
    token.delete()
    return redirect('homepage')
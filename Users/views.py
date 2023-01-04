from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import CustomCreateUserForm, ProfileForm
from .models import CustomUserModel, Profile, Token
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    fields = ['user','email','bio','last_name','first_name','location','website','phone','user_pic']
    
class ProfileUpdateView(UserPassesTestMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'
    
   
    def test_func(self):
        return self.get_object().user.id == self.request.user.id
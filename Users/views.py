from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import UserCreateForm, ProfileForm, UserLoginForm
from .models import CustomUserModel, Profile, Token
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class CreateUserView(CreateView):
    form_class = UserCreateForm
    template_name: str = 'registration/signup.html'
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base')
        else:
            return super().get(self, *args, **kwargs)
        
class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name: str = 'registration/login.html'
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base')
        else:
            return super().get(self, *args, **kwargs)
    def get_success_url(self) -> str:
        return reverse('profile', kwargs={'slug': self.request.user.profile.slug})

def email_verify(request, slug):
    try:
        token = get_object_or_404(Token, token = slug)
        CustomUserModel.objects.filter(id = token.user.id ).update(
            email_verification = True
        )
        token.delete()
        messages.success(request,'Emailingiz Tastiqlandi')
    except:
        messages.success(request,'Xatolik Yuz berdi Uzur Suraymiz')
    return redirect('base')

class ProfileView(DetailView):
    model = Profile
    template_name = 'account/profile.html'
    def get_queryset(self):
        return super().get_queryset().select_related('user')
    
    
class ProfileUpdateView(UserPassesTestMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'account/profile_edit.html'
    
    def test_func(self):
        return self.get_object().user.id == self.request.user.id

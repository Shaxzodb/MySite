from typing import Any, Dict
from django.views.generic import CreateView, DetailView, UpdateView
from .models import CustomUserModel, Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProfileForm
from Posts.forms import PostForm
from Posts.models import PostModel
from django.http import HttpResponseRedirect

from allauth.account.views import LoginView as AllauthLoginView,SignupView as AllauthSignupView

# Create your views here
# class ProfileView(UpdateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'account/profile.html'

#     # def test_func(self):
#     #     return self.get_object().user == self.request.user

#     # def handle_no_permission(self):
#     #     return render(self.request,'403.html')

#     def get_queryset(self):
#         return super().get_queryset().select_related('user')

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         return super().get_context_data(**kwargs)
from allauth.account.utils import get_next_redirect_url

class LoginView(AllauthLoginView):
    def form_valid(self, form):
        self.user = form.user # Get the forms user
        return super().form_valid(form)

    def get_success_url(self):
        ret = (
            get_next_redirect_url(self.request, self.redirect_field_name) or
            reverse('profile', kwargs={'slug': self.user.profile.slug})
        )
        return ret

class SignupView(AllauthSignupView):

    def get_success_url(self):
        ret = (
            get_next_redirect_url(self.request, self.redirect_field_name) or
            reverse('profile', kwargs={'slug': self.user.profile.slug})
        )
        return ret

from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return reverse('profile', kwargs={'slug': request.user.profile.slug})

class ProfileView(DetailView):
    model = Profile
    #form_class = ProfileForm
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(slug = self.kwargs['slug'])
        user = Profile.objects.filter(slug = self.kwargs['slug'])

        posts = PostModel.objects.filter(user = user[0].user.id)

        try:
            my_user = Profile.objects.get(id = self.request.user.id)
            user_friend = my_user.friends.filter(id = user[0].user.id).exists()
        except:
            user_friend = False
        context['form'] = ProfileForm(instance = profile)
        context['post_form'] = PostForm()
        context['posts'] = posts
        context['friend_config'] = user_friend
        return context
    def get_queryset(self):
        return super().get_queryset().select_related('user')

@login_required()
def user_data_save(request, slug):
    profile = Profile.objects.get(id = request.user.id)
    form = ProfileForm(request.POST, request.FILES, instance = profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return redirect('profile', request.user.profile.slug)

@login_required()
def friends(request, slug):
    if request.method == 'POST':
        user_profile = get_object_or_404(Profile, slug=slug)
        if request.user.profile.friends.filter(id = user_profile.user.id).exists():
            request.user.profile.friends.remove(user_profile.user)
        else:
            request.user.profile.friends.add(user_profile.user)
    return HttpResponseRedirect(reverse('profile', args=[str(slug)]))

@login_required()
def friends_remove(request, slug):
    user_profile = Profile.objects.get(slug = request.user.profile.slug)
    if request.method == 'POST':


        user = Profile.objects.get(slug=slug)
        if user_profile.friends.filter(id = user.user.id).exists():
            user_profile.friends.remove(user.user)

    return HttpResponseRedirect(reverse('profile', args=[str(user_profile.user.profile.slug)]))


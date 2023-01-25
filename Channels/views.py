from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, \
    DetailView, UpdateView, CreateView
from .models import Channel, Post
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Max
from .forms import ChannelCreateForm, PostCreateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Users.models import CustomUserModel, Profile
# Create your views here.


class ChannelView(ListView):
    model = Channel
    template_name = 'channel/channel_page.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.annotate(max_subscribers=Max('subscribers')).values().order_by('-max_subscribers', '-created_ch')


class ChannelDetailView(DetailView):
    model = Channel
    template_name = 'channel/channel_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(
            Channel,
            slug=self.kwargs['slug']
        )

        forms = PostCreateForm()
        context['form'] = forms
        sub = stuff.subscribers.filter(id=self.request.user.id).exists()
        context["subscribers"] = sub
        return context

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            channel = Channel.objects.get(slug=self.kwargs['slug'])
            form = PostCreateForm(
                self.request.POST
            )
            if form.is_valid():
                Post.objects.create(
                    author=self.request.user,
                    channel=channel,
                    content_pt=self.request.POST['content_pt'],
                )
            else:
                pass
        return redirect('channel', self.kwargs['slug'])


@login_required()
def channel_create(request):
    if request.method == "POST":
        form = ChannelCreateForm(request.POST)
        if form.is_valid():
            slug = request.POST.get('slug')
            if slug == '':
                slug = None
            channel = Channel.objects.create(
                name=request.POST.get('name'),
                owner=request.user,
                slug=slug,
                image_ch=request.POST.get('image_ch')
            )
        else:
            messages.info(request, form.errors)
            return redirect('profile', request.user.profile.slug)
        return HttpResponseRedirect(reverse('channel', args=[str(channel.slug)]))
    else:
        return HttpResponseRedirect(reverse('profile', args=[str(request.user.profile.slug)]))


class ChannelSittings(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Channel
    fields = ['name', 'image_ch', 'slug']
    template_name = 'channel/channel_sittings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(
            Channel,
            slug=self.kwargs['slug']
        )
        users = [users[0] for users in CustomUserModel.objects.all().values_list(
            'username') if stuff.owner.username != users[0]]
        context['users'] = users
        return context

    def test_func(self):
        return self.get_object().owner.id == self.request.user.id


@login_required()
def channel_delete(request, slug):
    if request.method == 'POST':
        channel = get_object_or_404(Channel, slug=slug)
        if request.user.id == channel.owner.id:
            channel.delete()
    return redirect('profile', request.user.profile.slug)


@login_required()
def subscribers(request, slug):
    if request.method == 'POST':
        sub = get_object_or_404(Channel, slug=slug)
        if sub.subscribers.filter(id=request.user.id).exists():
            sub.subscribers.remove(request.user)
        else:
            sub.subscribers.add(request.user)
    return HttpResponseRedirect(reverse('channel', args=[str(slug)]))


@login_required()
def channel_add_admin(request, slug):
    if request.method == 'POST':
        get_channel = get_object_or_404(Channel, slug=slug)
        if get_channel.owner.id == request.user.id and not get_channel.admins.filter(id=request.user.id).exists():
            get_user = CustomUserModel.objects.filter(
                username=request.POST['add_admin'])
            if get_user.exists() and not get_user[0] == get_channel.owner:
                get_channel.admins.add(get_user[0])
            else:
                messages.info(request, 'bunday foydalanuvchi topilmadi')
    return redirect('channel_sittings', slug)


@login_required()
def channel_remove_admin(request, user, channel):

    get_channel = get_object_or_404(Channel, slug=channel)
    if get_channel.owner.id == request.user.id and get_channel.admins.filter(id=request.user.id).exists():
        get_user = Profile.objects.filter(slug=user)
        if get_user.exists() and not get_user[0] == get_channel.owner:
            get_channel.admins.remove(get_user[0].user)
        else:
            messages.info(request, 'bunday Admin mavjud emas')
    return redirect('channel_sittings', channel)
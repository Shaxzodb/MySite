from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, \
    DetailView, UpdateView, CreateView
from .models import Channel, Post
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.db.models import Count, Max
from .forms import ChannelCreateForm, PostCreateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Users.models import CustomUserModel, Profile
from django.utils.html import format_html
from rest_framework.generics import ListAPIView
from .serializes import ChannelSerialize
# Create your views here.

class ChannelListApi(ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerialize
    
    
    

class ChannelView(ListView):
    model = Channel
    template_name = 'channel/channel_page.html'
    
    def get_queryset(self):
        qs = super().get_queryset().select_related('owner')
        return qs.annotate(max_subscribers=Count('subscribers')).order_by('-max_subscribers', '-created')


class ChannelDetailView(DetailView):
    model = Channel
    template_name = 'channel/channel_detail.html'
    
    def get_queryset(self):
        return super().get_queryset().all().select_related('owner')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sub = False
        admin = False
        if self.request.user.is_authenticated:
            
            stuff = get_object_or_404(
                Channel,
                slug=self.kwargs['slug']
            )
            admin = stuff.admins.filter(id = self.request.user.id).exists()
            sub = stuff.subscribers.filter(id=self.request.user.id).exists()
        forms = PostCreateForm()
        context['form'] = forms
        context['admin'] = admin
        
        context["subscribers"] = sub
        return context
    
@login_required()
def save_post(request,slug):
    if request.method=='POST':
        
        channel = get_object_or_404(
            Channel,
            slug=slug
        )
            
        if channel.admins.filter(id = request.user.id).exists() or channel.owner.id == request.user.id:
            form = PostCreateForm(
                request.POST
            )
                
            if form.is_valid():
                    
                   
                    
              Post.objects.create(
                author=request.user,
                channel=channel,
                content=request.POST['content'],
                        
                )
                  
                                     
    return redirect('channel', slug)
        


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
    fields = ['name', 'image_ch', 'slug', 'description']
    template_name = 'channel/channel_sittings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(
            Channel,
            slug=self.kwargs['slug']
        )
        admin = stuff.admins.filter(id = self.request.user.id).exists()
        users = [users[0] for users in CustomUserModel.objects.all().values_list(
            'username') if stuff.owner.username != users[0]]
        context['users'] = users
        return context

    def test_func(self):
        channel = Channel.objects.get(slug=self.kwargs['slug'])
        if channel.admins.filter(id = self.request.user.id).exists():
            return True
        return self.get_object().owner.id == self.request.user.id


@login_required()
def channel_delete(request, slug):
    if request.method == 'POST':
        channel = get_object_or_404(Channel, slug=slug)
        if request.user.id == channel.owner.id:
            channel.delete()
    return redirect('profile', request.user.profile.slug)

@login_required()
def post_delete(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        if request.user.id == post.author.id or post.channel.owner.id == request.user.id:
            post.delete()
    return redirect('channel', post.channel.slug)

class Edit_PostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = 'channel/post_edit.html'
    model = Post
    fields =['content']
    def post(self, *args, **kwargs):
        
        
        post = Post.objects.filter(id=kwargs['pk'])
        if not post[0].changed:
            post.update(changed=True)
        return super().post(self)
    def test_func(self):
        return self.get_object().author == self.request.user
    
    def get_success_url(self):
        post = Post.objects.get(id=self.kwargs['pk'])
   
        return reverse('channel', args=[str(post.channel.slug)])



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
                messages.info(request, f'{get_user[0].username} adminlar ro\'yxatiga qo\'shildi')
            else:
                messages.info(request, 'Bunday foydalanuvchi topilmadi')
    return redirect('channel_sittings', slug)


@login_required()
def channel_remove_admin(request, user, channel):

    get_channel = get_object_or_404(Channel, slug=channel)
    get_user = Profile.objects.filter(slug=user)
   
    if get_channel.owner.id == request.user.id and get_channel.admins.filter(id=get_user[0].user.id).exists():
        if get_user.exists() and not get_user[0] == get_channel.owner:
            get_channel.admins.remove(get_user[0].user)
            messages.info(request, f'{get_user[0].user.username} olib tashlandi')
        else:
            messages.info(request, 'Bunday admin mavjud emas')
        return redirect('channel_sittings', channel)
    if get_channel.admins.filter(id = request.user.id).exists():
        get_channel.admins.remove(get_user[0].user)
        messages.info(request, format_html(f'{get_user[0].user.username} Siz <strong>{get_channel.name}</strong> kanali adminligidan chiqdingiz.'))
       
    return redirect('channel', get_channel.slug)
    
@login_required()
def channel_remove_follower(request, user, channel):
    get_channel = get_object_or_404(Channel, slug=channel)
    get_user = Profile.objects.filter(slug=user)
    if get_channel.admins.filter(id = request.user.id).exists() or get_channel.owner.id == request.user.id:
        if get_user.exists() and not get_user == get_channel.owner:
            get_channel.subscribers.remove(get_user[0].user)
            messages.info(request, f'{get_user[0].user.username} olib tashlandi')
        else:
            messages.info(request, 'Bunday foydalanuvchi mavjud emas')
    return redirect('channel', channel)
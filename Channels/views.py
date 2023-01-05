from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Channel

# Create your views here.
class ChannelView(ListView):
    model = Channel
    template_name = 'channel/channel_page.html'
    def get_queryset(self):
        qs =  super().get_queryset()
        return qs.all().order_by('subscribers', '-created_ch')
class ChannelDetailView(DetailView):
    model = Channel
    template_name = 'channel/channel_detail.html'
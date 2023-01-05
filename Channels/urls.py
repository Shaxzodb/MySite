from django.urls import path
from .views import ChannelView, ChannelDetailView
urlpatterns = [
    path('channels/', ChannelView.as_view(), name = 'channels'),
    path('channel/<slug:slug>', ChannelDetailView.as_view(), name = 'channel'),
]

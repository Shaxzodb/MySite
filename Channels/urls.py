from django.urls import path
from .views import ChannelView, ChannelDetailView,\
    ChannelEdit, subscribers, channel_create, channel_delete
urlpatterns = [
    path('channels/', ChannelView.as_view(), name = 'channels'),
    path('channel/<slug:slug>', ChannelDetailView.as_view(), name = 'channel'),
    path('channel-edit/<slug:slug>/', ChannelEdit.as_view(), name = 'channel_edit'),
    path('subscribers/<slug:slug>', subscribers, name = 'subscribers'),
    path('channel-create/', channel_create, name = 'channel_create'),
    path('channel-delete/<slug:slug>/', channel_delete, name = 'channel_delete'),
]

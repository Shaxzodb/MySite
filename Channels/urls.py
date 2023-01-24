from django.urls import path
from .views import ChannelView, ChannelDetailView,\
    ChannelSittings, subscribers, channel_create, channel_delete,\
    channel_add_admin, channel_remove_admin
urlpatterns = [
    path('channels/', ChannelView.as_view(), name = 'channels'),
    path('channel/<slug:slug>', ChannelDetailView.as_view(), name = 'channel'),
    path('channel-sittings/<slug:slug>/', ChannelSittings.as_view(), name = 'channel_sittings'),
    path('subscribers/<slug:slug>', subscribers, name = 'subscribers'),
    path('channel-create/', channel_create, name = 'channel_create'),
    path('channel-delete/<slug:slug>/', channel_delete, name = 'channel_delete'),
    path('channel-add-admin/<slug:slug>/', channel_add_admin, name = 'channel_add_admin'),
    path('channel-remove-admin/<slug:user>/<slug:channel>', channel_remove_admin, name = 'channel_remove_admin'),
]

from django.urls import path
from .views import ChannelView, ChannelDetailView
urlpatterns = [
    path('channels/', ChannelView.as_view(), name = 'channels'),
    path('channels/<slug:slug>', ChannelDetailView.as_view(), name = 'channel'),
]

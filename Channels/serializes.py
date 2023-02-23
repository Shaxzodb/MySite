from rest_framework.serializers import ModelSerializer
from .models import Channel
class ChannelSerialize(ModelSerializer):
    class Meta:
        model = Channel
        fields = ['name','total_subscribers']
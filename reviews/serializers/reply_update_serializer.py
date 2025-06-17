from rest_framework import serializers
from ..models import Reply

class ReplyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['text']

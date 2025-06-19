from rest_framework import serializers
from ...models import Reply

class ReplyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'text', 'review_id']

    def create(self, validated_data):
        # Automatically set the user_id to the current user
        validated_data['user_id'] = self.context['request'].user
        return super().create(validated_data)

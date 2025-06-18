from rest_framework import serializers
from ..models import Review

class ReviewDisplaySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user_id.username')
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    is_liked = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'prof_id', 'module_code', 'text', 'rating', 
                  'username', 'likes_count', 'is_liked', 'can_edit', 'timestamp']

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        if user and user.is_authenticated:
            return obj.likes.filter(id=user.id).exists()
        return False
    
    def get_can_edit(self, obj):
        user = self.context['request'].user
        return user.is_authenticated and (obj.user_id == user or user.is_staff)

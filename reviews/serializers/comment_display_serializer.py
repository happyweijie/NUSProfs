from rest_framework import serializers

class CommentDisplaySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user_id.username', read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    is_liked = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()

    class Meta:
        model = None # Set in subclasses
        fields = ['id', 'username', 'text', 'likes_count', 'is_liked', 'can_edit', 'timestamp']

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return user.is_authenticated and obj.likes.filter(id=user.id).exists()

    def get_can_edit(self, obj):
        user = self.context['request'].user
        return user.is_authenticated and (obj.user_id == user or user.is_staff)
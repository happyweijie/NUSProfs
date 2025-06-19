from ..common import CommentDisplaySerializer
from ...models import Review
from professors.models import Module
from rest_framework import serializers

class ReviewDisplaySerializer(CommentDisplaySerializer):

    module_name = serializers.CharField(source='module_code.name', read_only=True)
    reply_count = serializers.SerializerMethodField()

    class Meta(CommentDisplaySerializer.Meta):
        model = Review
        fields = CommentDisplaySerializer.Meta.fields + [
            'prof_id', 'module_code', 'module_name', 'reply_count', 'rating'
        ]

    def get_reply_count(self, obj):
        return obj.reply_count()
    
    def get_module_name(self, obj):
        return Module.objects.get(module_code=obj.module_code).name \
            if obj.module_code else None

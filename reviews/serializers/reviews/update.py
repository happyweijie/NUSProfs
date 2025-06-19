from rest_framework import serializers
from ...models import Review

class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'rating', 'module_code'] 
        read_only_fields = ['prof_id']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

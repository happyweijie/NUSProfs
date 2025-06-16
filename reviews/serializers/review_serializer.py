from rest_framework import serializers
from ..models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'prof_id', 'module_code', 'text', 'rating']

    def validate(self, data):
        # Ensure that a user cannot review the same professor for the same module more than once
        u_id = self.context['request'].user
        p_id = data.get('prof_id')
        mod_code = data.get('module_code')

        # Skip if updating the same review
        if self.instance:
            if (self.instance.prof_id == p_id and self.instance.module_code == mod_code):
                return data

        if Review.objects.filter(user_id=u_id, prof_id=p_id, module_code=mod_code).exists():
            raise serializers.ValidationError("You have already reviewed the professor for this module.")
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        return Review.objects.create(user_id=user, **validated_data)

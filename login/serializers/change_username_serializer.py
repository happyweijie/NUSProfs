from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator

User = get_user_model()

class ChangeUsernameSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UnicodeUsernameValidator()],
    )

    class Meta:
        model = User
        fields = ['username']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.save()
        return instance

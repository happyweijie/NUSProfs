from professors.models import Teaches
from rest_framework import serializers

class TeachesSerializer(serializers.ModelSerializer):
    module_name = serializers.CharField(source='module.name', read_only=True)
    module_code = serializers.CharField(source='module.module_code', read_only=True)

    class Meta:
        model = Teaches
        fields = ['module_code', 'module_name', 'semester']
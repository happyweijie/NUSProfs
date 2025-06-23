from ..models import Module
from rest_framework import serializers

class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ['module_code', 'name']

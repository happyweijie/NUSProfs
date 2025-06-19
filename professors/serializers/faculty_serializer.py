from rest_framework import serializers
from ..models import Faculty
from .department_serializer import DepartmentSerializer

class FacultySerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = Faculty
        fields = ['faculty_id', 'name', 'departments']

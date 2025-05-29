from rest_framework import serializers
from .models import *

# Summary Serializer (Home Page and Search Results) 
class ProfessorSummarySerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    class Meta:
        model = Professor
        fields = ['prof_id', 'name', 'title', 'average_rating', 'faculty', 'department']

    def get_average_rating(self, obj):
        return 4.50  # Placeholder

    def get_faculty(self, obj):
        return obj.department.faculty.name if obj.department and obj.department.faculty else None

    def get_department(self, obj):
        return obj.department.name if obj.department else None

# Faculty and Department Serializers
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['dept_id', 'name']
    
class FacultySerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = Faculty
        fields = ['faculty_id', 'name', 'departments']
    
# Profile Page Serializers
class TeachesSerializer(serializers.ModelSerializer):
    module_name = serializers.CharField(source='module.name', read_only=True)
    module_code = serializers.CharField(source='module.module_code', read_only=True)

    class Meta:
        model = Teaches
        fields = ['module_code', 'module_name', 'semester']

class ProfessorDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    teaching = TeachesSerializer(many=True, read_only=True)

    class Meta:
        model = Professor
        fields = [
            'prof_id', 'name', 'title', 'office', 'phone',
            'average_rating', 'faculty', 'department', 'teaching'
        ]

    def get_average_rating(self, obj):
        return 4.50  # Placeholder

    def get_faculty(self, obj):
        return obj.department.faculty.name if obj.department and obj.department.faculty else None

    def get_department(self, obj):
        return obj.department.name if obj.department else None


from rest_framework import serializers
from professors.models import Professor
import statistics

# Summary Serializer (Home Page and Search Results) 
class ProfessorSummarySerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    class Meta:
        model = Professor
        fields = ['prof_id', 'name', 'title', 'average_rating', 'faculty', 'department']

    def get_average_rating(self, obj):
        return obj.average_rating() 

    def get_faculty(self, obj):
        return obj.department.faculty.name if obj.department and obj.department.faculty else None

    def get_department(self, obj):
        return obj.department.name if obj.department else None
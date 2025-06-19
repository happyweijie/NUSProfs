from ..models import Professor
from .teaches_serializer import TeachesSerializer
from rest_framework import serializers

class ProfessorDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    teaching = TeachesSerializer(many=True, read_only=True)

    class Meta:
        model = Professor
        fields = [
            'prof_id', 'name', 'title', 'office', 'phone',
            'average_rating', 'review_count', 'faculty', 'department', 'teaching'
        ]

    def get_review_count(self, obj):
        return obj.review_count()
    
    def get_average_rating(self, obj):
        return round(obj.average_rating(), 2)

    def get_faculty(self, obj):
        return obj.department.faculty.name if obj.department and obj.department.faculty else None

    def get_department(self, obj):
        return obj.department.name if obj.department else None
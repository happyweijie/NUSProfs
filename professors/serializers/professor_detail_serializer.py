from ..models import Professor, Teaches
from .teaches_serializer import TeachesSerializer
from rest_framework import serializers
from collections import defaultdict

class ProfessorDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    teaching = serializers.SerializerMethodField()
    teaching_history = serializers.SerializerMethodField()

    class Meta:
        model = Professor
        fields = [
            'prof_id', 'name', 'title', 'office', 'phone',
            'average_rating', 'review_count', 'faculty', 
            'department', 'teaching', 'teaching_history'
        ]

    def get_review_count(self, obj):
        return obj.review_count()
    
    def get_average_rating(self, obj):
        return round(obj.average_rating(), 2)

    def get_faculty(self, obj):
        return obj.department.faculty.name if (obj.department and obj.department.faculty) else None

    def get_department(self, obj):
        return obj.department.name if obj.department else None
    
    def get_teaching(self, obj):
        teaches_queryset = obj.teaching.select_related('module') \
            .order_by('semester')
        return TeachesSerializer(teaches_queryset, many=True).data

    def get_teaching_history(self, obj):
        teaches_queryset = Teaches.objects.filter(prof=obj) \
            .order_by("semester") \
            .select_related('module')
        
        modules = defaultdict(lambda: {"module_name": "", "semesters": []})

        for teach in teaches_queryset:
            code = teach.module.module_code
            modules[code]["module_name"] = teach.module.name
            modules[code]["semesters"].append(str(teach.semester))

        return [
            {
                "module_code": code,
                "module_name": data["module_name"],
                "semesters": data["semesters"]
            }
            for code, data in modules.items()
        ]
    
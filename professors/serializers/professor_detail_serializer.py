from ..models import Teaches
from .teaches_serializer import TeachesSerializer
from .professor_summary_serializer import ProfessorSummarySerializer
from rest_framework import serializers
from collections import defaultdict

class ProfessorDetailSerializer(ProfessorSummarySerializer):
    review_count = serializers.SerializerMethodField()
    teaching = serializers.SerializerMethodField()
    teaching_history = serializers.SerializerMethodField()

    class Meta(ProfessorSummarySerializer.Meta):
        fields = ProfessorSummarySerializer.Meta.fields + [
            'office', 'phone',
            'review_count', 'teaching', 'teaching_history'
        ]

    def get_review_count(self, obj):
        return obj.review_count()

    def get_teaching(self, obj):
        teaches_queryset = obj.teaching.select_related('module').order_by('semester')
        return TeachesSerializer(teaches_queryset, many=True).data

    def get_teaching_history(self, obj):
        teaches_queryset = Teaches.objects.filter(prof=obj).order_by("semester").select_related('module')
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
    
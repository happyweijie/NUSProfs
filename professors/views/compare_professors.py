from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Module, Semester, Teaches
from ..serializers import ProfessorSummarySerializer

class CompareModuleProfessorsView(APIView):
    serializer_class = ProfessorSummarySerializer

    def get(self, request, module_code):
        module = Module.objects.filter(module_code__iexact=module_code).first()
        if not module:
            return Response({
                "detail": "Module not found."
                }, status=status.HTTP_404_NOT_FOUND)

        # Get semesters from the latest AY
        latest_semesters = Semester.latest_academic_year()

        # Get teaching records
        teaches = Teaches.objects.filter(
            module=module,
            semester__in=latest_semesters
        ).select_related('prof', 'semester')

        if not teaches.exists():
            return Response({
                "detail": f"{module.module_code} not offered in current academic year."
                }, status=status.HTTP_200_OK)

        # Group professors by semester
        result = {}
        for semester in latest_semesters:
            profs = [
                record.prof 
                for record in teaches 
                if record.semester.id == semester.id
                ]
            if profs:
                result[str(semester)] = self.serializer_class(profs, many=True).data

        return Response({
            "module": module.module_code,
            "name": module.name,
            "semesters": result
            }, status=status.HTTP_200_OK)

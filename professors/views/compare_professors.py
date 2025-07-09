from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Module, Semester, Teaches
from ..serializers import ProfessorSummarySerializer

class CompareProfessorsView(APIView):
    serializer_class = ProfessorSummarySerializer

    def get(self, request, module_code, year=None):
        module = Module.objects.filter(module_code__iexact=module_code).first()
        if not module:
            return Response({
                "detail": f"Module {module_code} not found."
                }, status=status.HTTP_404_NOT_FOUND)

        # Get AY
        ay = Semester.get_academic_year(year) if year else Semester.latest_academic_year()
        if not ay:
            return Response({
                "detail": "No teaching records found for the specified academic year."
                }, status=status.HTTP_404_NOT_FOUND)


        # Get teaching records
        teaching_records = Teaches.objects.filter(
            module=module,
            semester__in=ay
        ).select_related('prof', 'semester')

        if not teaching_records.exists():
            return Response({
                "detail": f"{module.module_code} not offered in current academic year."
                }, status=status.HTTP_200_OK)

        # Group professors by semester
        result = {}
        for semester in ay:
            profs = [
                record.prof 
                for record in teaching_records
                if record.semester.id == semester.id
                ]
            if profs:
                result[str(semester)] = self.serializer_class(profs, many=True).data

        return Response({
            "module_code": module.module_code,
            "name": module.name,
            "semesters": result
            }, status=status.HTTP_200_OK)

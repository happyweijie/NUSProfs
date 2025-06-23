from ..models import Professor
from ..serializers import ProfessorSummarySerializer
from rest_framework.generics import GenericAPIView

class ProfessorSearchView(GenericAPIView):
    """
    View to handle search requests for professors.
    """
    serializer_class = ProfessorSummarySerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '').strip()
        departments = [
            int(dept_id) 
            for dept_id in request.query_params.get('departments', '').split(',') 
            if dept_id.isdigit()
        ]
        faculties = [
            int(faculty_id)
            for faculty_id in request.query_params.get('faculties', '').split(',')
            if faculty_id.isdigit()
        ]

        results = Professor.objects. \
            filter_by(query, departments, faculties). \
            order_by('name')

        result_page = self.paginate_queryset(results)
        serializer = self.get_serializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)
    
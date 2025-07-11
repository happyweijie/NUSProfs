from django.core.cache import cache
from django.utils.http import urlencode
from ..models import Professor
from ..serializers import ProfessorSummarySerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class ProfessorSearchView(GenericAPIView):
    """
    View to handle search requests for professors. Filter by name, department, and faculty.

    Supports pagination and returns a list of professors matching the search criteria.
    """
    serializer_class = ProfessorSummarySerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '').strip()
        departments = request.query_params.get('departments', '')
        faculties = request.query_params.get('faculties', '')
        page = request.query_params.get('page', '')

        params = {
            'q': query,
            'departments': departments,
            'faculties': faculties,
            'page': page,
        }

        # Make a cache key from params and check for cache
        key = f"professor_search:{urlencode(params)}"
        cached = cache.get(key)
        if cached:
            return Response(cached)

        # Apply filters
        department_ids = [int(d) for d in departments.split(',') if d.isdigit()]
        faculty_ids = [int(f) for f in faculties.split(',') if f.isdigit()]

        results = Professor.objects.filter_by(query, department_ids, faculty_ids) \
            .order_by('name')
        
        result_page = self.paginate_queryset(results)
        serializer = self.get_serializer(result_page, many=True)
        response = self.get_paginated_response(serializer.data)

         # Cache for 5 minutes
        cache.set(key, response.data, timeout=60*1)

        return response
    
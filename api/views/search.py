from professors.models import Professor
from professors.serializers import ProfessorSummarySerializer
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

SEARCH_LIMIT = 20

# Search feature
@api_view(['GET'])
def search(request):
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

    paginator = PageNumberPagination()
    paginator.page_size = SEARCH_LIMIT
    result_page = paginator.paginate_queryset(results, request)
    serializer = ProfessorSummarySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
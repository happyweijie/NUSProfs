from professors.models import Professor
from professors.serializers import ProfessorSummarySerializer
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.conf import settings

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
    # 20 to fall back on if not set in settings 
    paginator.page_size = settings.REST_FRAMEWORK.get('PAGE_SIZE', 20) 
    result_page = paginator.paginate_queryset(results, request)
    serializer = ProfessorSummarySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

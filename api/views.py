from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from professors.models import Professor, Faculty, Department
from professors.serializers import *
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

SEARCH_LIMIT = 20

def index(request):
    return render(request, "api/index.html", {
        "faculties": Faculty.objects.all().order_by('name'),
        "departments": Department.objects.all().order_by('name'),
    })

@api_view(['GET'])
def professor(request, prof_id):
    try:
        prof = Professor.objects.get(prof_id=prof_id)
    except Professor.DoesNotExist:
        return JsonResponse({"error": "Professor not found"}, status=404)
    
    return JsonResponse(ProfessorDetailSerializer(prof).data, safe=False)

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

    results = Professor.objects.filter_by(query, departments, faculties).order_by('name')

    paginator = PageNumberPagination()
    paginator.page_size = SEARCH_LIMIT
    result_page = paginator.paginate_queryset(results, request)
    serializer = ProfessorSummarySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def faculties(request):
    faculties = Faculty.objects.all().order_by('name')
    serializer = FacultySerializer(faculties, many=True)
    return JsonResponse(serializer.data, safe=False)

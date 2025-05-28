from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from professors.models import Professor, Faculty, Department
from professors.serializers import ProfessorSummarySerializer, ProfessorDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

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
    results = Professor.objects.filter(name__icontains=query).order_by('name')
    
    paginator = PageNumberPagination()
    paginator.page_size = 20
    result_page = paginator.paginate_queryset(results, request)
    serializer = ProfessorSummarySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

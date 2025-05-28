from django.shortcuts import render
from django.http import JsonResponse
from .models import Professor, Teaches, Module, Department, Faculty
from .serializers import ProfessorSummarySerializer, ProfessorDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

# Create your views here.
def index(request):
    return render(request, "professors/index.html")

@api_view(['GET'])
def all_professors(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    professors = Professor.objects.all().order_by('name')
    result_page = paginator.paginate_queryset(professors, request)
    serializer = ProfessorSummarySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

def professor(request, prof_id):
    try:
        prof = Professor.objects.get(prof_id=prof_id)
    except Professor.DoesNotExist:
        return JsonResponse({"error": "Professor not found"}, status=404)
    
    return JsonResponse(ProfessorDetailSerializer(prof).data, safe=False)

@api_view(['GET'])
def search(request):
    query = request.query_params.get('q', '').strip()
    results = Professor.objects.filter(name__icontains=query).order_by('name')
    
    paginator = PageNumberPagination()
    paginator.page_size = 20
    result_page = paginator.paginate_queryset(results, request)
    serializer = ProfessorSummarySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
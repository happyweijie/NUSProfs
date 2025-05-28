from django.shortcuts import render
from django.http import JsonResponse
from .models import Professor, Teaches, Module, Department, Faculty
from .serializers import ProfessorSummarySerializer, ProfessorDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

# Create your views here.
def index(request):
    return render(request, "professors/index.html", {
        "faculties": Faculty.objects.all().order_by('name'),
        "departments": Department.objects.all().order_by('name'),
    })

@api_view(['GET'])
def all_professors(request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    professors = Professor.objects.all().order_by('name')
    result_page = paginator.paginate_queryset(professors, request)
    serializer = ProfessorSummarySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

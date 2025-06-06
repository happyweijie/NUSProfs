from django.shortcuts import render
from django.http import JsonResponse
from .models import Professor, Teaches, Module, Department, Faculty
from .serializers import ProfessorSummarySerializer, ProfessorDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from .models import Professor, Teaches, Module, Department, Faculty

# Create your views here.
def index(request):
    return render(request, "professors/index.html", {
        "professors": Professor.objects.all(),
    })

def all_professors(request):
    professors = Professor.objects.all().order_by('name')
    return JsonResponse({
        "professors": [prof.summary() for prof in professors]
    })

def professors(request, prof_id):
    try:
        prof = Professor.objects.get(prof_id=prof_id)
    except Professor.DoesNotExist:
        return JsonResponse({"error": "Professor not found"}, status=404)
    
    return JsonResponse({
        "professor": prof.serialize(),
    })
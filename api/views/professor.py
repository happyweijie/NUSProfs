from django.http import JsonResponse
from rest_framework.decorators import api_view
from professors.models import Professor
from professors.serializers import ProfessorDetailSerializer

WARNING = {
    "deprecated": True,
    "message": "This endpoint is deprecated. Please use professors/prof_id instead." 
    }

@api_view(['GET'])
def professor(request, prof_id):
    try:
        prof = Professor.objects.get(prof_id=prof_id)
    except Professor.DoesNotExist:
        return JsonResponse({
            "error": "Professor not found",
            **WARNING
        }, status=404)

    return JsonResponse({
        **ProfessorDetailSerializer(prof).data,
        **WARNING
    }, safe=False)

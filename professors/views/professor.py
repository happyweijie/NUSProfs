from django.http import JsonResponse
from ..models import Professor
from ..serializers import ProfessorDetailSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def professor(request, prof_id):
    try:
        prof = Professor.objects.get(prof_id=prof_id)
    except Professor.DoesNotExist:
        return JsonResponse({"error": "Professor not found"}, status=404)
    
    return JsonResponse(ProfessorDetailSerializer(prof).data, safe=False)

from django.http import JsonResponse
from professors.models import Faculty
from professors.serializers import FacultySerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def faculties(request):
    faculties = Faculty.objects.all().order_by('name')
    serializer = FacultySerializer(faculties, many=True)
    return JsonResponse(serializer.data, safe=False)

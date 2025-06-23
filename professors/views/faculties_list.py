from rest_framework.generics import ListAPIView
from ..models import Faculty
from ..serializers import FacultySerializer

class FacultyListView(ListAPIView):
    serializer_class = FacultySerializer
    pagination_class = None
    queryset = Faculty.objects.all().order_by('name')

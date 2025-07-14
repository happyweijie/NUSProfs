from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from ..models import Faculty
from django.core.cache import cache
from ..serializers import FacultySerializer

class FacultyListView(ListAPIView):
    """
    View to list all faculties. Frontend should preferably cache this data.
    """
    CACHE_KEY = "faculty_list"
    serializer_class = FacultySerializer
    pagination_class = None
    queryset = Faculty.objects.all().order_by('name')

    def list(self, request, *args, **kwargs):   
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data:
            print("Using cache for Faculty List")
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set(self.CACHE_KEY, data, timeout=None)
        print("Set cache for Faculty List")

        return Response(data)

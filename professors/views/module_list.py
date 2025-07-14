from ..serializers import ModuleSerializer
from ..models import Module
from django.core.cache import cache
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

class ModuleListView(ListAPIView):
    """
    View to list all modules. Frontend should preferably cache this data.
    """
    CACHE_KEY = "all_modules_list"
    serializer_class = ModuleSerializer
    pagination_class = None  # No pagination for this view

    def get_queryset(self):
        return Module.objects.all() \
            .order_by('module_code')
    
    def list(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)
        if cached_data:
            print("Using existing cache for modules list")
            return Response(cached_data)

        # If cache miss, generate response data
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # Cache the serialized data
        cache.set(self.CACHE_KEY, data, timeout=None)
        print("Set cache for modules list")

        return Response(data)

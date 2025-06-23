from ..serializers import ModuleSerializer
from ..models import Module
from rest_framework.generics import ListAPIView

class ModuleListView(ListAPIView):
    """
    View to list all modules. Frontend should preferably cache this data.
    """
    serializer_class = ModuleSerializer
    pagination_class = None  # No pagination for this view

    def get_queryset(self):
        return Module.objects.all() \
            .order_by('module_code')

from rest_framework.generics import RetrieveAPIView
from ..models import Professor
from ..serializers import ProfessorDetailSerializer

class ProfessorDetailsView(RetrieveAPIView):
    """
    View to retrieve details of a specific professor by their ID.
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorDetailSerializer
    lookup_field = 'prof_id' 

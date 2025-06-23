from rest_framework.generics import RetrieveAPIView
from ..models import Professor
from ..serializers import ProfessorDetailSerializer

class ProfessorDetailsView(RetrieveAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorDetailSerializer
    lookup_field = 'prof_id' 

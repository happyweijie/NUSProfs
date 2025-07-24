from ..models import Professor
from ..serializers import ProfessorSummarySerializer
from django.db.models import Avg
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError

DEFAULT_N = 10

class TopProfessorsView(ListAPIView):
    serializer_class = ProfessorSummarySerializer

    def get_queryset(self):
        n = self.request.query_params.get('n', DEFAULT_N)
        try:
            n = int(n)
            if n <= 0:
                raise ValueError("n must be at least 1")
        except ValueError:
            raise ValidationError("Query parameter 'n' must be a positive integer.")

        return Professor.objects.annotate(avg_rating=Avg('reviews__rating')) \
                                .filter(avg_rating__isnull=False) \
                                .order_by('-avg_rating')[:n]

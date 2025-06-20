from ..models import Professor
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ReviewSummaryView(APIView):
    def get(self, request, prof_id):
        professor = get_object_or_404(Professor, pk=prof_id)

        return Response({
            "average_rating": professor.average_rating(),
            "review_count": professor.review_count()
        })
    
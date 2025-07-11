from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Semester

@method_decorator(cache_page(60 * 60 * 24 * 30), name='dispatch')  # Cache for 30 days
class AcademicYearListView(APIView):
    def get(self, request):
        # Get distinct ay_start values
        years = (
            Semester.objects.values_list("ay_start", flat=True)
            .distinct()
            .order_by("-ay_start")
        )

        # Format them into {"value": 2024, "label": "AY24/25"}
        data = [
            {
                "label": Semester.format_ay(year),
                "value": year, 
                }
            for year in years
        ]

        return Response({
            "academic_years": data
            })

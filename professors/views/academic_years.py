from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Semester

class AcademicYearListView(APIView):
    def get(self, request):
        cached = cache.get("academic_year_list")
        if cached:
            print("Using existing cache for AY list")
            return Response(cached)

        # Get distinct ay_start values
        years = (
            Semester.objects.values_list("ay_start", flat=True)
            .distinct()
            .order_by("-ay_start")
        )

        response_data = {
            "academic_years": [
                {
                    "label": Semester.format_ay(year),
                    "value": year, 
                    }
                for year in years
            ]
        }
        # set cache
        cache.set("academic_year_list", response_data, timeout=None)
        print("Set cache for AY list")
        
        return Response(response_data)
    
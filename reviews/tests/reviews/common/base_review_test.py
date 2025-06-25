from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from reviews.models.review import Review
from professors.models import Faculty, Department, Professor, Module

User = get_user_model()

class BaseReviewTestCase(APITestCase):
    def setUp(self):
        # Create Users
        self.user = User.objects.create_user(username='testuser', password='TestPass123')
        self.other_user = User.objects.create_user(username='otheruser', password='TestPass456')

        # Create Authenticated Client
        self.client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        # Create Faculty/Department/Professor
        self.sci_faculty = Faculty.objects.create(name="Science")
        self.math_dept = Department.objects.create(name="Math", faculty=self.sci_faculty)
        self.jteo = Professor.objects.create(
            name="Jonathon Teo",
            department=self.math_dept,
            title="Lecturer",
            office="S1-01-01",
            phone="12345678"
        )

        # Create Module
        self.module = Module.objects.create(module_code="MA1522", name="Linear Algebra")

        self.data = {
            "prof_id": self.jteo.prof_id,
            "module_code": self.module.module_code,
            "rating": 4.5,
            "text": "Great prof!"
        }


from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..common import ProfessorCommonData
from ...models import Professor, Module, Faculty, Department
from reviews.models import Review

User = get_user_model()

class TopProfessorsTest(APITestCase):
    def setUp(self):

        self.url = reverse("professors:top_professors")

        # User
        self.user = User.objects.create(username="tester", password="P@55W0RD")

        # Faculty and Department
        self.science = Faculty.objects.create(name="Science")
        self.math = Department.objects.create(name="Math", faculty=self.science)

        # Module
        self.module = Module.objects.create(module_code="MA1522", name="Math")

        # Ratings
        self.ratings = [5, 4, 4, 3, 3, 3, 3, 2, 1, 1]

        # Create 10 professors
        for i in range(10):
            prof = Professor.objects.create(
                name=f"Prof {i}",
                department=self.math,
                title="Lecturer",
                office="S1-01-01",
                phone="12345678"
                )

            # Add reviews with ratings
            Review.objects.create(
                user_id=self.user,
                prof_id=prof,
                module_code=self.module,
                rating=self.ratings[i], 
                text="test")

    def test_n(self):
        for i in range(1, 6):
            response = self.client.get(self.url, {'n': i})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["count"], i)

    def test_default_n(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data["count"], 10)
    
    def test_negative_n(self):
        response = self.client.get(self.url, {'n': -800})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_str_n(self):
        response = self.client.get(self.url, {'n': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_top_professor(self):
        response = self.client.get(self.url, {'n': 1})
        top_prof = response.data["results"][0]
        self.assertEqual(top_prof["name"], "Prof 0")
        self.assertEqual(top_prof["average_rating"], 5.0)

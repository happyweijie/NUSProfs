from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Professor, Department, Faculty

class ProfessorDetailsViewTest(APITestCase):
    def setUp(self):
        self.faculty = Faculty.objects.create(name="Computing")
        self.department = Department.objects.create(name="Computer Science", faculty=self.faculty)
        self.prof = Professor.objects.create(
            name="Dr Jane Doe",
            department=self.department,
            title="Associate Professor",
            office="COM1-01-01",
            phone="12345678"
        )
        self.valid_url = reverse("professors:professor", args=[self.prof.prof_id])
        self.invalid_url = reverse("professors:professor", args=[99999])  # ID that does not exist

    def test_get_valid_professor(self):
        response = self.client.get(self.valid_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Dr Jane Doe")
        self.assertEqual(response.data['title'], "Associate Professor")

    def test_get_invalid_professor(self):
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", response.data)

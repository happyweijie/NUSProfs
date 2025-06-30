from django.test import TestCase
from django.contrib.auth import get_user_model
from ...models import Faculty, Department, Professor, Module
from ...serializers import ProfessorDetailSerializer, ProfessorSummarySerializer
from reviews.models import Review

User = get_user_model()

class ProfessorSerializerTest(TestCase):
    def setUp(self):
        self.serializer = None
        self.faculty = Faculty.objects.create(name="Computing")
        self.department = Department.objects.create(name="Computer Science", faculty=self.faculty)
        self.prof = Professor.objects.create(
            name="Dr Jane Doe",
            department=self.department,
            title="Associate Professor",
            office="COM1-01-01",
            phone="12345678"
        )

        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword"
        )

        self.module1 = Module.objects.create(
            module_code="CS1010",
            name="Programming Methodology",
        )
        self.module2 = Module.objects.create(
            module_code="CS1020",
            name="Data Structures and Algorithms",
        )

    # Test Serializer Fields
    def test_average_rating(self):
        Review.objects.create(
            prof_id=self.prof,
            user_id=self.user,
            module_code=self.module1,
            text="Great professor!",
            rating=4
        )
        Review.objects.create(
            prof_id=self.prof,
            user_id=self.user,
            module_code=self.module2,
            text="Excellent course!",
            rating=5
        )

        serializer = self.serializer(self.prof)
        data = serializer.data

        self.assertEqual(data["average_rating"], 4.5)

    def test_department_name(self):
        serializer = self.serializer(self.prof)
        data = serializer.data

        self.assertEqual(data["department"], "Computer Science")

    def test_faculty_name(self):
        serializer = self.serializer(self.prof)
        data = serializer.data

        self.assertEqual(data["faculty"], "Computing")

class ProfessorDetailSerializerTest(ProfessorSerializerTest):
    def setUp(self):
        super().setUp()
        self.serializer = ProfessorDetailSerializer

class ProfessorSummarySerializerTest(ProfessorSerializerTest):
    def setUp(self):
        super().setUp()
        self.serializer = ProfessorSummarySerializer
from django.test import TestCase
from ...models import Faculty, Department, Professor

class ProfessorCommonData(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.science = Faculty.objects.create(name="Science")
        cls.computing = Faculty.objects.create(name="Computing")

        cls.math = Department.objects.create(name="Math", faculty=cls.science)
        cls.cs = Department.objects.create(name="Computer Science", faculty=cls.computing)

        cls.j_teo = Professor.objects.create(
            name="Jonathon Teo",
            department=cls.math,
            title="Lecturer",
            office="S1-01-01",
            phone="12345678"
        )

        cls.j_mark = Professor.objects.create(
            name="Jonathan Scarlett",
            department=cls.cs,
            title="Associate Professor",
            office="C1-01-01",
            phone="87654321"
        )
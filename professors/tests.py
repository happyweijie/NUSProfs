from django.test import TestCase

# Create your tests here.
from .models import Professor, Faculty, Department, Module, Teaches

class ProfessorsTestCase(TestCase):
    def setUp(self):
        # create dummy faculty and department
        com = Faculty.objects.create(name="Computing")
        sci = Faculty.objects.create(name="Science")

        cs_dept = Department.objects.create(name="Computer Science", faculty=com)
        math_dept = Department.objects.create(name="Mathematics", faculty=sci)

        # create dummy professors
        alice = Professor.objects.create(name="Alice Smith", department=cs_dept, title="Senior Lecturer", office="COM1-01-01", phone="12345678")
        bob = Professor.objects.create(name="Bob Johnson", department=math_dept, title="Associate Professor", office="COM2-02-02", phone="87654321")
        charlie = Professor.objects.create(name="Charlie Johnston", department=cs_dept, title="Professor", office="COM1-03-03", phone="11223344")

        # dummy modules
        cs1010 = Module.objects.create(module_code="CS1010", name="Programming Methodology")
        ma1102r = Module.objects.create(module_code="MA1101R", name="Calculus") 
        cs2040 = Module.objects.create(module_code="CS2040", name="Data Structures and Algorithms")

        # dummy teaches relationships
        Teaches.objects.create(prof=alice, module=cs1010, semester="Semester 1")
        Teaches.objects.create(prof=bob, module=ma1102r, semester="Semester 2")
        Teaches.objects.create(prof=charlie, module=cs1010, semester="Semester 1")

    def test_professor_count(self):
        d1 = Department.objects.get(name="Computer Science")
        d2 = Department.objects.get(name="Mathematics")

        self.assertEqual(d1.professors.count(), 2)
        self.assertEqual(d2.professors.count(), 1)

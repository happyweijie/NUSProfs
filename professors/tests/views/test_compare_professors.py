from rest_framework.test import APITestCase
from rest_framework import status
from professors.models import Module, Professor, Semester, Teaches
from django.urls import reverse

class CompareProfessorsTestCase(APITestCase):
    def setUp(self):
        self.sem1 = Semester.objects.create(ay_start=2024, semester_number=1)
        self.sem2 = Semester.objects.create(ay_start=2024, semester_number=2)

    def test_invalid_ay(self):
        module = Module.objects.create(module_code="CS9999", name="Ghost Module")
        response = self.get_response(module_code=module)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", response.data)

    def test_module_not_found(self):
        # Invalid module
        invalid_code = "INVALID1234"
        response = self.get_response(module_code=invalid_code)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", response.data)

    def test_module_not_offered_in_latest_ay(self):
        # Module not taught by anyone
        module = Module.objects.create(module_code="CS9999", name="Ghost Module")

        # Get response
        response = self.get_response(module_code=module.module_code)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["detail"], 
            f"{module.module_code} not offered in current academic year."
            )
        
    def test_module_only_in_sem1(self):
        # Module taught only in sem1
        module = Module.objects.create(module_code="CS1010", name="Programming")
        prof = Professor.objects.create(name="Prof Sem1")
        Teaches.objects.create(prof=prof, module=module, semester=self.sem1)

        # Get response
        response = self.get_response(module_code=module.module_code)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("semesters", response.data)
        self.assertIn(str(self.sem1), response.data["semesters"])

    def test_module_only_in_sem2(self):
        # Module taught only in sem1
        module = Module.objects.create(module_code="CS1010", name="Programming")
        prof = Professor.objects.create(name="Prof Sem2")
        Teaches.objects.create(prof=prof, module=module, semester=self.sem2)

        # Get response
        response = self.get_response(module_code=module.module_code)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("semesters", response.data)
        self.assertIn(str(self.sem2), response.data["semesters"])

    def test_module_in_both_semesters(self):
        # Module taught in both Semesters
        module = Module.objects.create(module_code="CS2030", name="OO Programming")

        prof1 = Professor.objects.create(name="Prof A")
        prof2 = Professor.objects.create(name="Prof B")
        Teaches.objects.create(prof=prof1, module=module, semester=self.sem1)
        Teaches.objects.create(prof=prof2, module=module, semester=self.sem2)

        response = self.get_response(module_code=module.module_code)

        self.assertEqual(response.status_code, 200)
        # Check semester 1 and 2 is recorded
        self.assertIn(str(self.sem1), response.data["semesters"])
        self.assertEqual(prof1.prof_id, response.data["semesters"][str(self.sem1)][0]["prof_id"])
        self.assertIn(str(self.sem2), response.data["semesters"])
        self.assertEqual(prof2.prof_id, response.data["semesters"][str(self.sem2)][0]["prof_id"])

        # Check correct professor counts
        self.assertEqual(len(response.data["semesters"][str(self.sem1)]), 1)
        self.assertEqual(len(response.data["semesters"][str(self.sem2)]), 1)
    
    def test_same_professor_in_both_semesters(self):
        module = Module.objects.create(module_code="CS2040", name="Data Structures")
        prof = Professor.objects.create(name="Prof Repeat")
        Teaches.objects.create(prof=prof, module=module, semester=self.sem1)
        Teaches.objects.create(prof=prof, module=module, semester=self.sem2)

        response = self.get_response(module_code=module.module_code)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["semesters"][str(self.sem1)]), 1)
        self.assertEqual(len(response.data["semesters"][str(self.sem2)]), 1)

    def get_response(self, module_code, year=None):
        # Get response
        if not year:
            url = reverse("professors:compare-professors-latest", args=[module_code])
        else:
            url = reverse("professors:compare-professors-year", args=[module_code, year])

        return self.client.get(url)
    
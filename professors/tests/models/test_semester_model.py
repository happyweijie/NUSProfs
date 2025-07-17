from django.test import TestCase
from ...models import Semester
from django.core.exceptions import ValidationError

class SemesterModelTest(TestCase):
    def setUp(self):
        # Create various semesters
        Semester.objects.create(ay_start=2022, semester_number=1)  # 22/23 Semester 1
        Semester.objects.create(ay_start=2022, semester_number=2)  # 22/23 Semester 2
        Semester.objects.create(ay_start=2022, semester_number=3)  # 22/23 Special Term I
        Semester.objects.create(ay_start=2023, semester_number=1)  # 23/24 Semester 1
        Semester.objects.create(ay_start=2023, semester_number=4)  # 23/24 Special Term II

    def test_format_ay(self):
        self.assertEqual(Semester.format_ay(2022), "AY22/23")
        self.assertEqual(Semester.format_ay(2024), "AY24/25")

    def test_str_method(self):
        sem = Semester.objects.get(ay_start=2022, semester_number=3)
        self.assertEqual(str(sem), "AY22/23 Special Term I")

    def test_unique_constraint(self):
        with self.assertRaises(Exception):
            Semester.objects.create(ay_start=2022, semester_number=1) 

    def test_ordering(self):
        semesters = Semester.objects.all()
        ordered = list(semesters)
        self.assertTrue(ordered[0].ay_start >= ordered[1].ay_start)

    def test_latest_academic_year(self):
        latest = Semester.latest_academic_year()
        self.assertEqual(len(latest), 2)
        self.assertEqual(latest[0].ay_start, 2023)

    def test_get_academic_year(self):
        sems_2022 = Semester.get_academic_year(2022)
        self.assertEqual(len(sems_2022), 3)
        self.assertTrue(all(s.ay_start == 2022 for s in sems_2022))

    def test_clean_method_invalid_semester(self):
        # Semester number not in allowed choices (e.g., 5)
        s = Semester(ay_start=2025, semester_number=5)
        with self.assertRaises(ValidationError) as context:
            s.clean()

        self.assertIn("Invalid semester number", str(context.exception))

    def test_clean_method_valid_semester(self):
        # Valid semester numbers: 1–4
        valid_semesters = [1, 2, 3, 4]
        for num in valid_semesters:
            s = Semester(ay_start=2025, semester_number=num)
            try:
                s.clean() 
            except ValidationError:
                self.fail(f"Unexpected ValidationError for semester {num}")

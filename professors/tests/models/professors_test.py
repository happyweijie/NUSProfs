from ...models import Professor
from ..common import ProfessorCommonData

class ProfessorModelTest(ProfessorCommonData):
    def setUp(self):
        return super().setUp()
    
    def test_filter_by_name(self):
        # Tests filter by method used for search directly
        results = Professor.objects.filter_by("Jon", [], [])
        assert self.j_teo in results
        assert self.j_mark in results

    def test_filter_by_faculty(self):
        # Tests filter by method used for search directly
        results = Professor.objects.filter_by(
            name_query="Jon", faculty_ids=[self.science.faculty_id], department_ids=[])
        assert self.j_teo in results
        assert self.j_mark not in results

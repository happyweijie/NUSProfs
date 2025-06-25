from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..common import ProfessorCommonData
from ...models import Professor

class ProfessorSearchViewTest(ProfessorCommonData):
    def setUp(self):
        self.url = reverse("professors:search") 

    def test_filter_by_method(self):
        # Tests filter by method used for search directly
        results = Professor.objects.filter_by("Jon", [], [])
        assert self.j_teo in results
        assert self.j_mark in results

    def test_search_by_name_jon(self):
        response = self.client.get(self.url, {'q': 'jon'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        names = [prof['name'] for prof in response.data['results']]
        self.assertIn("Jonathon Teo", names)
        self.assertIn("Jonathan Scarlett", names)
        self.assertEqual(len(names), 2)

    def test_filter_by_department(self):
        response = self.client.get(self.url, {
            'q': 'jon',
            'departments': str(self.cs.dept_id)
        })
        names = [prof['name'] for prof in response.data['results']]
        self.assertIn("Jonathan Scarlett", names)
        self.assertNotIn("Jonathon Teo", names)
        
    def test_filter_by_faculty(self):
        response = self.client.get(self.url, {
            'q': 'jon',
            'faculties': str(self.science.faculty_id)
        })
        names = [prof['name'] for prof in response.data['results']]
        self.assertIn("Jonathon Teo", names)
        self.assertNotIn("Jonathan Scarlett", names)

    def test_filter_by_both_department_and_faculty(self):
        response = self.client.get(self.url, {
            'q': 'jon',
            'departments': str(self.cs.dept_id),
            'faculties': str(self.computing.faculty_id)
        })
        names = [prof['name'] for prof in response.data['results']]
        self.assertIn("Jonathan Scarlett", names)

    def test_no_results(self):
        response = self.client.get(self.url, {'q': 'xyz'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], [])
        self.assertEqual(response.data['count'], 0)

    def test_search_pagination(self):
        # Should have 22 now
        for i in range(20):
            Professor.objects.create(
                name=f"Prof {i}", 
                department=self.cs,
                title="Associate Professor",
                office="abc",
                phone="87654321"
                )
         
        response = self.client.get(self.url, {'q': '', })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 22)
        self.assertEqual(len(response.data["results"]), 20) # first page

    def test_search_pagination_page_two(self):
        # Should have 22 now
        for i in range(20):
            Professor.objects.create(
                name=f"Prof {i}", 
                department=self.cs,
                title="Associate Professor",
                office="abc",
                phone="87654321"
                )
         
        response = self.client.get(self.url, {'q': '', 'page': 2, })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 22)
        self.assertEqual(len(response.data["results"]), 2)

    def test_search_pagination_invalid_page(self):
        # Should have 22 now
        response = self.client.get(self.url, {'q': '', 'page': 999, })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", response.data) # verify error message
    
    
from django.http import response
from django.test import TestCase, SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_pages_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_pages_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

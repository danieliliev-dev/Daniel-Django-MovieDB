from django.test import TestCase
from django.urls import reverse

class MovieTests(TestCase):

    def test_movie_category_invalid(self):
        # Test if an invalid category triggers the right error page (404, not 5XX)
        response = self.client.get(reverse('movie_category', args=['invalid-category']))
        self.assertEqual(response.status_code, 404)  # Ensure it's a 404 error, not a 5XX


from django.test import TestCase # db involved
from django.test import SimpleTestCase # When no db is needed


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


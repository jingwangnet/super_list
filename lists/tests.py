from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import home_page

# Create your tests here.
class HomePageTest(TestCase):


    def test_can_resolve_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_can_return_correct_content(self):
        request = HttpRequest()
        response = home_page(request)
        content = response.content.decode()

        self.assertTrue(content.startswith('<html>'), content)
        self.assertIn('<title>To-Do lists</title>', content)
        self.assertTrue(content.endswith('</html>'), content)
        

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import home_page

# Create your tests here.
class HomePageTest(TestCase):


    def test_home_page_can_return_correct_content(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/index.html')

    def test_home_page_can_save_a_post_request(self):
        context = {'new-item': 'A new item'}
        response = self.client.post('/', data=context)
        html = response.content.decode()

        self.assertIn(context['new-item'], html)
        self.assertTemplateUsed(response, 'lists/index.html')
        

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import home_page
from .models import Item

# Create your tests here.
class HomePageTest(TestCase):


    def test_home_page_can_return_correct_content(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/index.html')

    def test_home_page_can_save_a_post_request(self):
        context = {'new-item': 'A new item'}
        response = self.client.post('/', data=context)
        html = response.content.decode()

        self.assertEqual(1, Item.objects.count())
        item = Item.objects.first()
        self.assertEqual(item.text, context['new-item'])

        self.assertIn(context['new-item'], html)
        self.assertTemplateUsed(response, 'lists/index.html')
        

class ItemAndListTest(TestCase):


    def test_start_two_item_and_retrieve_it_later(self):
        first_item = Item()
        first_item.text = 'first item'
        first_item.save()

        second_item = Item()
        second_item.text = 'second item'
        second_item.save()

        saved_item = Item.objects.all()
        self.assertEqual(2, len(saved_item))

        first_saved_item, second_saved_item = saved_item

        self.assertEqual(first_saved_item.text, 'first item')
        self.assertEqual(second_saved_item.text, 'second item')

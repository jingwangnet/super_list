from django.test import TestCase
from lists.models import Item, List

class ItemAndListTest(TestCase):


    def test_start_two_item_and_retrieve_it_later(self):
        list_ = List.objects.create()
        first_item = Item()
        first_item.text = 'first item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'second item'
        second_item.list = list_
        second_item.save()

        saved_item = list_.item_set.all()
        self.assertEqual(2, len(saved_item))

        first_saved_item, second_saved_item = saved_item

        self.assertEqual(first_saved_item.text, 'first item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'second item')
        self.assertEqual(second_saved_item.list, list_)

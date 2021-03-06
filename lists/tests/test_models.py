from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError

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

    def test_cant_save_empty_list_item(self):
        list_ = List.objects.create() 
        item = Item(text='', list=list_)
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_get_absolute_url(self):
        list_ = List.objects.create() 
        self.assertEqual(list_.get_absolute_url(), f'/list/{list_.pk}/')
    
    def test_duplicate_item_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')      
 
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='bla')
            item.full_clean()
   
    def test_can_save_same_item_to_diffrent_ilist(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')      
        item = Item(list=list2, text='bla')
        item.full_clean()  # Dont shout raise error

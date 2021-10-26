from lists.forms import ItemForm, ExistingListItemForm
from lists.models import List, Item
from django.test import TestCase


class ItemFormTest(TestCase):
    

    def test_form_item_input_has_placeholder_and_name_and_id(self):
        itemform = ItemForm()
        self.assertIn('type="text"', itemform.as_p())
        self.assertIn('id="id-new-item"', itemform.as_p())
        self.assertIn('placeholder="Submit a item for saving"', itemform.as_p())

    def test_form_item_validation_for_blank_item(self):
        itemform = ItemForm(data={"new-text":''})
        self.assertFalse(itemform.is_valid())
        self.assertIn(
            "You can't save an empty item",
            itemform.errors['text']
        )
    
    def test_form_saving_handels_a_list(self): 
        list_ = List.objects.create()
        itemform = ItemForm(data={'text': 'do it'})
        itemform.save(for_list=list_) 
       
        
       
class ExistingListItemFormTest(TestCase):
    

    def test_form_item_input_has_placeholder_and_name_and_id(self):
        list_ = List.objects.create()
        itemform = ExistingListItemForm(for_list=list_)
        self.assertIn('type="text"', itemform.as_p())
        self.assertIn('id="id-new-item"', itemform.as_p())
        self.assertIn('placeholder="Submit a item for saving"', itemform.as_p())

    def test_form_item_validation_for_blank_item(self):
        list_ = List.objects.create()
        itemform = ExistingListItemForm(for_list=list_, data={'text': ''})
        self.assertFalse(itemform.is_valid())
        self.assertIn(
            "You can't save an empty item",
            itemform.errors['text']
        )
    
    def test_form_validation_for_duplicate_items(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='no twins')
        itemform = ExistingListItemForm(for_list=list_, data={'text':'no twins'})
        self.assertFalse(itemform.is_valid())
        self.assertEqual(itemform.errors['text'], ["You've already got this in your list"])
 
    def test_form_save(self):
       list_ = List.objects.create()
       itemform = ExistingListItemForm(for_list=list_, data={'text': 'hi'})
       new_item = itemform.save()
       self.assertEqual(new_item, Item.objects.first()) 
       


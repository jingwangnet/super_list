from lists.forms import ItemForm
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
    
       
        
       


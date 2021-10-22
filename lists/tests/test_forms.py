from lists.forms import ItemForm
from django.test import TestCase

class ItemFormTest(TestCase):
    

    def test_form_item_input_has_placeholder_and_name_and_id(self):
        itemform = ItemForm()
        self.assertIn('type="text"', itemform.as_p())
        self.assertIn('name="new-item"', itemform.as_p())
        self.assertIn('id="id-new-item"', itemform.as_p())
        self.assertIn('placeholder="Submit a item for saving"', itemform.as_p())


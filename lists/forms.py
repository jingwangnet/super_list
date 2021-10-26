from django import forms
from lists.models import Item
from django.core.exceptions import ValidationError

FIELD_NAME_MAPPING = {
    'text': 'new-item',
}

class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
            'id': 'id-new-item',
            'placeholder': 'Submit a item for saving'
            }),
        }
        error_messages = {
            'text': {
                'required': "You can't save an empty item",
            },
        }
 
    def save(self, for_list, *args, **kwargs):
        self.instance.list = for_list
        return super().save(*args, **kwargs)
                
    
class ExistingListItemForm(ItemForm):
    
    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list
   
    def validate_unique(self):
        try: 
            self.instance.validate_unique()
        except ValidationError as e:   
            e.error_dict = {'text': ["You've already got this in your list"]}
            self._update_errors(e)
    
    def save(self, *args, **kwargs):
        return super(forms.models.ModelForm, self).save(*args, **kwargs)

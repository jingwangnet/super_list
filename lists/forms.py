from django import forms
from lists.models import Item

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
                
    

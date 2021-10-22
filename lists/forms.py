from django import forms
from lists.models import Item

FIELD_NAME_MAPPING = {
    'text': 'new-item',
}

class ItemForm(forms.models.ModelForm):
    def add_prefix(self, field_name):
        field_name =  FIELD_NAME_MAPPING.get(field_name, field_name)
        return super().add_prefix(field_name)

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
    

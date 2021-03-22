from django import forms
from .models import items


class ItemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ['name', 'done']

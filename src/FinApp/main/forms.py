from .models import InputField, Category
from django.forms import *


class FieldForm(ModelForm):
    """Form for spends"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Select your category"

    class Meta:
        model = InputField
        fields = ["title", "amount", "date", "cat"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'What were spent on'
            }),
            "amount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the amount'
            }),
            "date": SelectDateWidget(),
            "cat": Select()
        }


class CatForm(ModelForm):
    """Form for category's"""

    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'What were spent on'
            })
        }


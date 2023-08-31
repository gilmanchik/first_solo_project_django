from .models import *
from django.forms import ModelForm, TextInput, Textarea


class InformationForm(ModelForm):
    class Meta:
        model = Information
        fields = ['title', 'description']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),

            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            })
        }

from .models import *
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),

            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),

            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),

            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            })

        }

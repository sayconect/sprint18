from .models import Author
from django.forms import ModelForm, TextInput


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control mb-4 mr-sm-2 col-md-3',
                'placeholder': 'name'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control mb-4 mr-sm-2 col-md-3',
                'placeholder': 'surname',
            }),
            'patronymic': TextInput(attrs={
                'class': 'form-control mb-4 mr-sm-2 col-md-3',
                'placeholder': 'patronymic'
            }),
        }

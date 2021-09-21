from django import forms
from django.forms import fields, TextInput
from .models import CustomUser
class UsersFrom(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password', 'role', 'is_active' ]

        widgets = {
            'first_name': TextInput(attrs={

                'placeholder': 'first_name'
            }),
            'middle_name': TextInput(attrs={

                'placeholder': 'middle_name',
            }),
            'last_name': TextInput(attrs={

                'placeholder': 'last_name'
            }),
            'email': TextInput(attrs={

                'placeholder': 'email'
            }),
            'password': TextInput(attrs={

                'placeholder': 'password',
            }),
        }

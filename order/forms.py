from .models import Order
from django import forms
from book.models import Book
from authentication.models import CustomUser


class OrderForm(forms.Form):
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all(), empty_label='Choose the user', label='User', widget=forms.Select(attrs={'class': 'form-control'}))
    book = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label='Choose the book', label='Book', widget=forms.Select(attrs={'class': 'form-control'}))
    plated_end_at = forms.DateTimeField(label='Plated at (YYYY-MM-DD HH:MM:SS)', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}))
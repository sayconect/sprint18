from author.models import Author
from django.db.models import fields
from .models import Book
from typing import Counter
from django import forms

class BooksForm(forms.Form):
    # class Meta:
    #     model = Book
    #     fields = ['name', 'description', 'count', 'authors']

    name = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea, required=True)
    count = forms.IntegerField(initial=10)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

    def save(self):
        new_tag = Book.objects.create(name=self.cleaned_data['name'],
                                      description = self.cleaned_data['description'],
                                      count=self.cleaned_data['count']
                                      )
        new_tag.authors.set(self.cleaned_data['authors'])
        return new_tag
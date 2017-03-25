from django import forms
from .models import Publisher, Book, BookFormat
from django.forms import modelform_factory
from django_countries import countries


class BookFormatForm(forms.ModelForm):
    """
    Not used (experimental)
    """
    class Meta:
        model = BookFormat
        fields = ['book_format']


class Book(forms.ModelForm):
    """
    Not used (experimental)
    """
    class Meta:
        model = Book
        fields = ['title', 'pub_date', 'format']


class PublisherForm(forms.ModelForm):
    """
    Not used (experimental)
    """
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'city', 'state', 'country', 'website']

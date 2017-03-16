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

"""
Not used (experiment using modelform_factory)
"""
publisher_form = modelform_factory(Publisher, fields=['name', 'address', 'city', 'state', 'country', 'website'],
                                   widgets={'country': forms.Select(choices=countries)})

"""
Not used (experiment using modelformset_factory)
"""
ModelPublisherFormset = forms.modelformset_factory(Publisher, fields=('name', 'website'), max_num=3, extra=2)
model_formset = ModelPublisherFormset(queryset=Publisher.objects.filter(name__startswith='S'))
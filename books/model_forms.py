from django import forms
from .models import Publisher, Book, BookFormat
from django.forms import modelform_factory
from django_countries import countries


class BookFormatForm(forms.ModelForm):
    class Meta:
        model = BookFormat
        fields = ['book_format']


class Book(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pub_date', 'format']


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'city', 'state', 'country', 'website']


publisher_form = modelform_factory(Publisher, fields=['name', 'address', 'city', 'state', 'country', 'website'],
                                   widgets={'country': forms.Select(choices=countries)})


ModelPublisherFormset = forms.modelformset_factory(Publisher, fields=('name', 'website'), max_num=3, extra=2)
model_formset = ModelPublisherFormset(queryset=Publisher.objects.filter(name__startswith='S'))
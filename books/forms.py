from django import forms
from .models import Book
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries
from crispy_forms.helper import FormHelper


# class PublisherModelChoiceField(forms.ModelChoiceField):
#     """
#     Use this derived Field class to change the display for a fiels
#     in case you control the fields in the Form.
#     """
#     def label_from_instance(self, obj):
#         return obj.name


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """
        Override to change the display for a Model(Multi)ChoiceField,
        using the field name and the 'label_from_instance' attribute.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.fields['publisher'].label_from_instance = lambda obj: "%s" % obj.name
        self.helper = FormHelper()

    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'pub_date', 'isbn', 'format', 'category', 'book_cover']


# NOT USED
class PublisherForm(forms.Form):
    name = forms.CharField(label="Publisher's name", max_length=30)
    address = forms.CharField(label="Address", max_length=50)
    country = LazyTypedChoiceField(choices=countries)
    state = forms.CharField(max_length=20)
    city = forms.CharField(max_length=30)
    website = forms.URLField()


PublishersFormSet = forms.formset_factory(PublisherForm, max_num=3)
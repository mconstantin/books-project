from django import forms

from .models import Book, Publisher, Author

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Layout, Div, Field, Fieldset, HTML
from crispy_forms.bootstrap import FormActions, PrependedText, InlineCheckboxes, InlineRadios


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
        self.fields['isbn'].label = 'ISBN'
        self.fields['format'].empty_label = None
        self.helper = FormHelper()
        self.helper.form_id = 'id-add-book-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'create-book'

        self.helper.layout = Layout(
            Field('title'),
            # see this SO for how to make the select and link appear inline: http://stackoverflow.com/a/31226655/2152249
            Div(
                Field('authors', style='display: inline-block;'),
                HTML("""<span class="input-group-btn"><a href="{% url 'create-author' %}" class="btn btn-link"><span class="glyphicon glyphicon-plus"></span></a></span>"""),
                css_class="input-group"
            ),
            Fieldset(
                'Publishing',
                Div(
                    Field('publisher', style='display: inline-block;'),
                    HTML(
                        """<span class="input-group-btn"><a href="{% url 'create-publisher' %}" class="btn btn-link"><span class="glyphicon glyphicon-plus"></span></a></span>"""),
                    css_class="input-group"
                ),
                # 'publisher',
                'pub_date'
            ),
            Fieldset(
                'Book Info',
                PrependedText('isbn', 'ISBN'),
                InlineRadios('format'),
                InlineCheckboxes('category'),
                'book_cover'
            ),
            FormActions(
                Submit('save', 'Save'),
                HTML("""<a href="{% url 'books' %}" class="btn btn-secondary">Cancel</a>""")
            )
        )
        # self.helper.add_input(Submit('submit', 'Save'))

    def clean_isbn(self):
        """
        Use this to prepend 'isbn' to the value enetered in the form.
        :return:
        """
        return 'isbn' + self.cleaned_data['isbn']

    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'pub_date', 'isbn', 'format', 'category', 'book_cover']


class PublisherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """
        Override to set the form.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-add-publisher-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'create-publisher'

        self.helper.layout = Layout(
            Field('name'),
            Fieldset(
                'Addrees Info',
                'address',
                'city',
                'state',
                'country'
            ),
            Field('website'),
            FormActions(
                Submit('save', 'Save'),
                HTML("""<a href="{% url 'create-book' %}" class="btn btn-secondary">Cancel</a>""")
            )
        )

    class Meta:
        model = Publisher
        fields = ['name', 'address', 'city', 'state', 'country', 'website']


class AuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """
        Override to set the form.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        # Two different ways to change a Field's label
        # either here using the label attribute for the filed in the 'fields' dictionary,
        # or in the Meta class, using "labels = { <field_name>: <label_name>, ...}" (see below).
        self.fields['born_at'].label = 'Born on'
        self.fields['died_at'].label = 'Died on'
        self.helper = FormHelper()
        self.helper.form_id = 'id-add-author-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'create-author'

        self.helper.layout = Layout(
            Field('first_name'),
            Field('middle_name'),
            Field('last_name'),
            Field('email'),
            Field('headshot', label="Picture"),
            Field('born_at'),
            Field('died_at'),
            FormActions(
                Submit('save', 'Save'),
                HTML("""<a href="{% url 'create-book' %}" class="btn btn-secondary">Cancel</a>""")
            )
        )

    class Meta:
        model = Author
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'headshot', 'born_at', 'died_at']

        labels = {
            'headshot': 'Picture',
        }
        help_texts = {
            'headshot': 'Upload a picture of the author',
        }


# NOT USED
PublishersFormSet = forms.formset_factory(PublisherForm, max_num=3)
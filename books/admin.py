from django.contrib import admin
from .models import Publisher, Author, Book, BookCategory, BookFormat


# class BooksInLine(admin.StackedInline):
class BooksInLine(admin.TabularInline):
    """
    Example of modifying the admin interface to show a list for a model in tabular form (multicolumn).
    """
    model = Book
    # add forms to add 2 additional books
    extra = 2
    # use 'fieldsets' to group the fields for the model, using a list of 2-tuples, where
    # first tuple element is the name of the fieldset (or None for empty), and the second is a
    # dictionary with 'fields' as the key and the list of model's fields as value.
    fieldsets = [
        (None, {'fields': ['title', 'authors']}),
        ("Publishing Information", {'fields': ['publisher', 'pub_date', 'isbn']}),
        ("Book Information", {'fields': ['format', 'category']})
    ]
    # add a filter on the right-hand site
    # Django sets predefined filters, e.g. last 7 days, etc.
    list_filter = ['pub_date']


class PublisherAdmin(admin.ModelAdmin):
    # list of display columns
    list_display = ['name', 'website', 'published_books', 'address', 'city', 'state', 'country']
    # 'fieldsets' grouping for an individual publisher
    fieldsets = [
        (None, {'fields': ['name', 'website']}),
        ('Address', {'fields': ['address', 'city', 'state', 'country']})
    ]
    # for a specific publisher, show the list of (its published) books, using the 'BooksInLine' UI above
    inlines = [BooksInLine]
    list_filter = ['name', 'city']


class BookAdmin(admin.ModelAdmin):
    model = Book
    fieldsets = [
        (None, {'fields': ['title', 'authors']}),
        ("Publishing Information", {'fields': ['publisher', 'pub_date', 'isbn']}),
        ("Book Information", {'fields': ['format', 'category']})
    ]
    list_display = ['title', 'authors_names', 'publisher_name', 'pub_date', 'isbn']
    list_filter = ['pub_date']

# register all the models with the corresponding new templates (if any), with the admin site
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author)
admin.site.register(BookCategory)
admin.site.register(BookFormat)
admin.site.register(Book, BookAdmin)
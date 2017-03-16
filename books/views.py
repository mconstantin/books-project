from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.forms import inlineformset_factory
from django.urls import reverse, reverse_lazy

from .models import Publisher, Author, Book, BookFormat
from .forms import BookForm, PublisherForm, AuthorForm
from .model_forms import publisher_form, model_formset


# Create your views here.
def index(request):
    """
    View function for home page of the site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    num_publishers = Publisher.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_authors': num_authors, 'num_publishers': num_publishers,
                 'num_visits': num_visits },
    )


class BookListView(generic.ListView):
    """
    Used for list of books view
    """
    model = Book


class BookDetailView(generic.DetailView):
    """
    Used for a single book view
    """
    model = Book


class CreateBookView(generic.edit.CreateView):
    """
    Used for viewing the form for creating a book
    """
    template_name = 'books/create_book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books')


class CreatePublisherView(generic.edit.CreateView):
    """
    Used for showing the form for creating a publisher
    """
    template_name = 'books/create_publisher.html'
    model = Publisher
    form_class = PublisherForm
    success_url = reverse_lazy('create-book')


class CreateAuthorView(generic.edit.CreateView):
    """
    Used for showing the form for creating an author
    """
    template_name = 'books/create_author.html'
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('create-book')


class AuthorListView(generic.ListView):
    """
    Used for showing the list of authors
    """
    model = Author


class AuthorDetailView(generic.DetailView):
    """
    Used for showing an author detail
    """
    model = Author


class PublisherListView(generic.ListView):
    """
    Used for showing the list of publishers
    """
    model = Publisher


class PublisherDetailView(generic.DetailView):
    """
    Used for showing a publisher detail
    """
    model = Publisher


# FORMS (experimental - NOT USED)
def get_publisher(request):
    if request.method == 'POST':
        form = publisher_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/done/')
    else:
        # a GET method
        form = publisher_form

    # return render(request, 'books/publisher-bootstrap.html', {'form': form})
    return render(request, 'books/publisher.html', {'form': form})


def manage_publishers2(request):
    initial = {'city': 'NY', 'state': 'NY', 'country': 'US'}
    if request.method == 'POST':
        formset = model_formset(request.POST)
        if formset.is_valid():
            pass
    else:
        formset = model_formset
    return render(request, 'books/manage_publishers.html', {'formset': formset})


def manage_books(request):
    BookInlineFormSet = inlineformset_factory(BookFormat, Book, fields=('title', 'format'))
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/done/')
    else:
        formset = BookInlineFormSet()
    return render(request, 'books/manage_books.html', {'formset': formset})
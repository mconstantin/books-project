from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Publisher, Author, Book
from .forms import BookForm, PublisherForm, AuthorForm


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

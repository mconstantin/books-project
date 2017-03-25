from django.test import TestCase, Client
from django.conf import settings

from books.models import Author, Publisher, Book, BookFormat, BookCategory


class BooksDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        scott = Author.objects.create(first_name='Scott', last_name='Fitzgerald', middle_name='F.')
        penguin_books = Publisher.objects.create(name='PenguinBooks', address='3 Wellington Plaza',
                                                website='www.penguin-books.uk', city='London', state='England',
                                                country='UK')
        hard = BookFormat.objects.create(book_format='hard')
        fiction = BookCategory.objects.create(category='fiction')
        classic = BookCategory.objects.create(category='classic')

        cls.book = cls.add_book("The Great Gatsby", (scott,), penguin_books, '1973-05-15', hard, (fiction, classic),
                                'ISBN821789174')

    def test_book_detail(self):
        r = self.client.get('/books/book/' + str(self.book.id))
        self.assertEqual(r.status_code, 200, 'request failed')
        # this fails to find the title.. it appears that it searches for a title like '\'Great Gatsby\'' !!!
        # self.assertContains(r, self.book.title.encode('utf-8'), count=1, html=True)
        self.assertIn(self.book.title, r.rendered_content, 'title not found')
        self.assertTemplateUsed(r, 'books/book_detail.html', 'wrong template used')

    @classmethod
    def add_book(cls, title, authors, publisher, pub_date, fmt, cat, isbn):
        book = Book()
        book.title = title
        book.publisher = publisher
        book.pub_date = pub_date
        book.format = fmt
        book.isbn = isbn
        book.save()
        try:
            iter(authors)
            book.authors.set(authors)
        except TypeError:
            book.authors.add(authors)
        try:
            iter(cat)
            book.category.set(cat)
        except TypeError:
            book.category.add(cat)
        return book



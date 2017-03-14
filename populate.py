import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booksProject.settings')
django.setup()

from books.models import Publisher, Author, Book, BookFormat, BookCategory


#python script for generating some sample data
#this script deletes all the data, before populating the new data

def populate():
    clear_data()

    # add publishers
    apress = add_publisher('Apress', '123 Main', 'http://www.apress.com', 'NY', 'NY', 'USA')
    mcgraw = add_publisher('McGraw-Hill', '345 Main', 'http://www.mcgrawhill.com', 'San Jose', 'CA', 'USA')
    british = add_publisher('British1', '678 Main', 'http://www.british1.com', 'London', 'England', 'UK')
    harper_collins = add_publisher('Harper-Collins', '123 Manhattan', 'www.harper-collins.com', 'NY', 'NY', 'US')
    random_house = add_publisher('Random House', '3445 Brooklyn', 'www.random-house.com', 'NY', 'NY', 'US')
    penguin_books = add_publisher('Penguin Books', '3 Wellington Plaza', 'www.penguin-books.uk', 'London', 'England', 'UK')
    simon_shuster = add_publisher('Simon & Shuster', '5th Ave Manhattan', 'www.simonandshuster.com', 'NY', 'NY', 'US')
    oreilly = add_publisher("O'Reilly", '1005 Graveinstein HW North', 'www.oreilly.com', 'Sebastopol', 'CA', 'US')
    harper_perrenial = add_publisher('Harper Perrenial', '123 7th St', 'wwww.harper-collins.com', 'NY', 'NY', 'US')

    # add authors
    marquez = add_author('Gabriel', 'Marquez', '1922-03-07', mname='Garcia', email='ggm@literature.nobel.org',
                         died_at='1988-12-22')
    twain = add_author('Mark', 'Twain', '1899-01-05', mname='Charles', email='mtwain@books.com', died_at='1956-09-08')
    elman = add_author('Julia', 'Elman', '1977-06-16')
    lavin = add_author('Mark', 'Lavin', '1973-11-19')
    holovety = add_author('Adrian', 'Holovety', '1984-12-25', email='adrianh@email.com')
    george = add_author('Nigel', 'George', '1969-03-11', email='ng@email.com')
    bennet = add_author('James', 'Bennet', '1956-09-01', email='jamesb@email.com')

    # add books
    hard = add_book_format('hard')
    soft = add_book_format('soft')
    kindle = add_book_format('kindle')

    fuction = add_book_category('fiction')
    non_fiction = add_book_category('non-fiction')
    techical = add_book_category('technical')
    travel = add_book_category('travel')
    education = add_book_category('education')
    religious = add_book_category('religious')
    modern = add_book_category('modern')
    classic = add_book_category('classic')
    poetry = add_book_category('poetry')

    add_book('One Hundered Years of Solitude', marquez, harper_collins, '1978-08-12', hard, (non_fiction, classic), 'isbn879812742')
    add_book('The Adventures of Hucklberry Finn', twain, penguin_books, '2015-07-25', soft, (non_fiction, classic), 'isbn535613465')
    add_book('Love in the Time of Cholera', marquez, harper_perrenial, '2007-10-05', soft, non_fiction, 'isbn090812333124')
    add_book('The Definitive Guide to Django', (elman, holovety), apress, '2015-08-04', soft, techical, 'isbn76376347862')
    add_book('Django CMS', george, apress, '2016-08-04', hard, techical, 'isbn7678678678')
    add_book('Lightweight Django', lavin, oreilly, '2014-11-13', kindle, techical, 'isbn898097878')

    # Print out what we have added to the user.
    for b in Book.objects.all():
        print("Book title: {}, Author(s): {}, Publisher: {}, publication date: {}"
              .format(b.title, '|'.join([a.first_name + ' ' + a.last_name for a in b.authors.all()]),
                      b.publisher.name, b.pub_date))


def clear_data():
    Publisher.objects.all().delete()
    Author.objects.all().delete()
    BookFormat.objects.all().delete()
    BookCategory.objects.all().delete()
    Book.objects.all().delete()


def add_author(fname, lname, born_at, mname=None, email=None, died_at=None, headshot=None):
    return Author.objects.create(first_name=fname, last_name=lname, middle_name=mname, email=email,
                                        born_at=born_at, died_at=died_at, headshot=headshot)


def add_publisher(name, address, website, city, state, country):
    return Publisher.objects.create(name=name, address=address, website=website,
                                           city=city, state=state, country=country)


def add_book_format(fmt):
    return BookFormat.objects.create(book_format=fmt)


def add_book_category(cat):
    return BookCategory.objects.create(category=cat)


def add_book(title, authors, publisher, pub_date, fmt, cat, isbn):
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


if __name__ == '__main__':
    print("Starting Books population script...")
    populate()
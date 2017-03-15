from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField


# Create your models here.
class Publisher(models.Model):
    """Publisher model"""
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    country = CountryField()
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return 'id={}, name={}, websites={}'.format(self.id, self.name, self.website)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the Publisher.
        """
        return reverse('publisher-detail', args=[str(self.id)])

    def published_books(self):
        return len(self.book_set.all())

    published_books.integer = True
    published_books.short_description = '# of published books'


class Author(models.Model):
    """
        Author Model
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    headshot = models.ImageField(upload_to='images', null=True, blank=True)
    born_at = models.DateField(null=True, blank=True)
    died_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return self.get_fullname()

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('author-detail', args=[str(self.id)])

    def get_fullname(self):
        return '{} {} {}'.format(self.first_name, self.middle_name if self.middle_name else '', self.last_name)


class BookFormat(models.Model):
    book_format = models.CharField(max_length=6)

    def __str__(self):
        return self.book_format


class BookCategory(models.Model):
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.category


class Book(models.Model):
    """
        Book Model
    """
    title = models.CharField(max_length=80)
    abstract = models.CharField(max_length=120, null=True, blank=True)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pub_date = models.DateField()
    isbn = models.CharField(max_length=30)
    book_cover = models.ImageField(upload_to='book_covers', null=True, blank=True)
    format = models.ForeignKey(BookFormat, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(BookCategory)
    ranking = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ["title", "pub_date"]

    def __str__(self):
        return 'id={}, {}, by {}, published {}'\
            .format(self.id, self.title, ', '.join([a.first_name + ' ' + a.last_name for a in self.authors.all()]),
                    self.publisher.name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('book-detail', args=[str(self.id)])

    def other_authors(self, an_author):
        return filter(lambda other_author: other_author != an_author, self.authors.all())

    def publisher_name(self):
        return self.publisher.name

    def authors_names(self):
        return ', '.join([a.first_name + ' ' + a.last_name for a in self.authors.all()])

    publisher_name.short_description = 'Publisher'
    authors_names.short_description = 'Authors'

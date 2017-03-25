from django.test import TestCase
import os
from django.core.files import File
from django.conf import settings

from books.models import Author


# Create your tests here
class AuthorTestCase(TestCase):
    STATIC_DIR = settings.STATIC_DIR
    MEDIA_DIR = settings.MEDIA_URL
    BASE_DIR = settings.BASE_DIR

    def setUp(self):
        Author.objects.create(first_name='Scott', last_name='Fitzgerald', middle_name='F.')

    def test_fullname(self):
        # from books.models import Author
        scott = Author.objects.get(last_name='Fitzgerald')
        self.assertEqual(scott.get_fullname(), 'Scott F. Fitzgerald', 'fullname does not match')

    def test_imageurl(self):
        # from books.models import Author
        scott = Author.objects.get(last_name='Fitzgerald')
        self.assertEqual(scott.image_url(), '/static/images/default_author.png', 'image url must be the default')
        headshot = os.path.join(self.STATIC_DIR, 'scottf.jpg')
        scott.headshot.save(os.path.basename(headshot), File(open(headshot, 'rb')))
        self.assertEqual(scott.image_url(), os.path.join(self.MEDIA_DIR, 'images', 'scottf.jpg'), 'image url is incorrect')
        os.remove(os.path.join(self.BASE_DIR, scott.image_url()[1:]))


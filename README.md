# books

[![N|Solid](https://www.djangoproject.com/s/img/logos/django-logo-negative.png)](https://www.djangoproject.com/)

*books* is a simple project as a newbie Django developer, written for a beginner course, around the idea of a bookstore.

* populate the database (default SQLite), by running the populate.py script
  * this requires some images: unzip the images.zip in its directory
* click on the links in the navbar (Books, Authors and Publishers) to see a list of those items populated in the database
* click on the __Add Book__ button on the top of the *Books List* to add a new book
  * in the "Add a Book" form, enter at least all the required fields; select an existing author(s) and/or publisher, or add a new one by clicking on the __+__ button next to the Author(s) or Publisher, respectively

Much functionality is still missing:
* delete items from the list
* edit items in the list
* adding a ranking to books and display the ranking average (prefereably using a '*****' style)
* etc.

The project has a couple of dependencies which must be installed.
#### [crispy forms](http://django-crispy-forms.readthedocs.io/en/latest/)
Install using:
```sh
pip install --upgrade django-crispy-forms
```
#### [django-countries](https://pypi.python.org/pypi/django-countries-plus)
Install using:
```sh
pip installl django-countries
```

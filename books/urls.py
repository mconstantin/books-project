from django.conf.urls import url

from books import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^books/create/$', views.CreateBookView.as_view(), name='create-book'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^author/create/$', views.CreateAuthorView.as_view(), name='create-author'),
    url(r'^publishers/$', views.PublisherListView.as_view(), name='publishers'),
    url(r'^publisher/(?P<pk>\d+)$', views.PublisherDetailView.as_view(), name='publisher-detail'),
    url(r'^publisher/create/$', views.CreatePublisherView.as_view(), name='create-publisher'),
    # FORMS (experimental - NOT USED)
    url(r'^forms/publisher/$', views.get_publisher, name='publisher_form'),
    # url(r'^forms/manage-publishers/$', manage_publishers, name='manage_publisher_form'),
    url(r'^forms/manage-publishers/$', views.manage_publishers2, name='manage_publisher_form'),
    url(r'^forms/books/$', views.manage_books, name='books_form'),
]
from factory.django import DjangoModelFactory
from api.models import Author, Book
from datetime import date


class AuthorFactory(DjangoModelFactory):

    first_name = 'John'
    last_name = 'Smith'

    class Meta:
        model = Author


class BookFactory(DjangoModelFactory):

    class Meta:
        model = Book
        django_get_or_create = ('publish_date', )
    publish_date = date.today()

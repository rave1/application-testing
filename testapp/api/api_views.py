from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer, UserSerializer


class AuthorAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = ()
    pagination_class = PageNumberPagination
    filter_backends = (filters.OrderingFilter, )
    ordering_fields = ('first_name', 'last_name', 'id')


class BookAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = ()
    pagination_class = PageNumberPagination


class AuthAuthorVIew(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated, )


class UserListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = ()

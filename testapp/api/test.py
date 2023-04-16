from rest_framework.test import APITestCase
from rest_framework import status

from api.models import Book, Author
from api.factory import AuthorFactory, BookFactory

from django.urls import reverse


class AuthorTestCase(APITestCase):

    def setUp(self) -> None:
        for i in range(10):
            AuthorFactory()
        for author in Author.objects.all():
            book = BookFactory(
                author=author
            )

    def test_author_permissions(self):
        url = reverse('auth-author')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_response(self):
        url = reverse('authors')
        response = self.client.get(url)
        list_of_keys = ['id', 'first_name', 'last_name']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data['results'][0].keys()), list_of_keys)

    def test_author_creation(self):
        url = reverse('authors')
        data = {'first_name': 'Martin', 'last_name': 'Luther'}
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 11, 'first_name': 'Martin', 'last_name': 'Luther'})
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
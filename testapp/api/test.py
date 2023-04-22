from rest_framework.test import APITestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from rest_framework import status

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'id': 11, 'first_name': 'Martin', 'last_name': 'Luther'})
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SeleniumTests(LiveServerTestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()


    def test_authors_selenium(self):
        from time import sleep
        driver = self.driver
        driver.get(f'http://127.0.0.1:8000{reverse("authors")}')
        first_name = driver.find_element(By.NAME, 'first_name')
        last_name = driver.find_element(By.NAME, 'last_name')
        sleep(1)
        first_name.send_keys('Radosław')
        sleep(1)
        last_name.send_keys('Paluch')
        sleep(3)        
        last_name.send_keys(Keys.RETURN)
        assert 'Radosław' in driver.page_source
        driver.get(f'http://127.0.0.1:8000{reverse("authors")}?ordering=-id')
        assert 'Paluch' in driver.page_source
        sleep(3)


    
    def test_login(self):
        from time import sleep
        driver = self.driver
        driver.get('http://127.0.0.1:8000/api/login/login/?next=/api/users/')
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        username.send_keys('admin')
        sleep(1)
        password.send_keys('admin')
        sleep(1)
        button = driver.find_element(By.NAME, 'submit')
        button.click()
        assert 'admin' in driver.page_source
        sleep(3)

    def test_book_template(self):
        from time import sleep
        driver = self.driver
        driver.get('http://localhost:8000/authors/')
        assert 'Radosław Paluch' in driver.page_source

    def tearDown(self) -> None:
        self.driver.close()

import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UsersCustomViewSet
from .models import Users

# Create your tests here.

class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_1234'
        self.email = 'adm@ya.ru'
        self.data = {
            'username': 'Администратор',
            'email': 'admin@ya.ru',
            'password': 'p@$$w0rD!',
            'first_name': 'Egorka',
            'last_name': 'Ostroumov',
        }
        self.data_put = {
            'username': 'Админ',
            'email': 'admin077@ya.ru',
            'password': 'p@$$w0rD!',
            'first_name': 'Egorka!',
            'last_name': 'Ostroumov!',
        }
        self.url = '/api/users/'
        self.admin = Users.objects.create_superuser(self.name, self.email, self.password)

    def test_get_list(self):
        #
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = UsersCustomViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # тест падает, так как по тех заданию, UsersCustomViewSet не имеет возможности создавать и удалять данные.
    # def test_create_guest(self):
    #     factory = APIRequestFactory()
    #     request = factory.post(self.url, self.data, format='json')
    #     view = UsersCustomViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # тест падает, так как по тех заданию, UsersCustomViewSet не имеет возможности создавать и удалять данные.
    # def test_create_admin(self):
    #     factory = APIRequestFactory()
    #     request = factory.post(self.url, self.data, format='json')
    #     force_authenticate(request, self.admin)
    #     view = UsersCustomViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def tearDown(self) -> None:
        pass
from django.test import TestCase
from requests import request
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from users_app.models import Users
from users_app.views import UsersModelViewSet
from .views import ProjectDjangoFilterViewSet, ToDoDjangoFilterViewSet
from .models import ToDo, Project
# Create your tests here.

class TestProjectViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'araym'
        self.password = 'z1mbabva'
        self.email = 'adm@ya.ru'
        self.data = {'project': 'testing','git_link': 'git.com', 'is_active': True,}
        self.data_put = {'project': 'test','git_link': 'git.com/proj_1', 'is_active': True,}
        self.users = {'username': 'user', 'password':'pass3124', 'email':'mail@mail.ru'}
        self.url_project = '/api/project/'
        self.url_users = '/api/users/'
        self.admin = Users.objects.create_superuser(self.name, self.email, self.password)

    def test_create_admin(self):
        # создаем админа:
        factory = APIRequestFactory()
        request = factory.post(self.url_users, self.users, format='json')
        force_authenticate(request, self.admin)
        view = UsersModelViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list(self):
        #список проектов:
        factory = APIRequestFactory()
        request = factory.get(self.url_project)
        view = ProjectDjangoFilterViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        # детализация проекта:
        client = APIClient()
        projects = Project.objects.create(**self.data)
        response = client.get(f'{self.url_project} {projects.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_object(self):
        client = APIClient()
        projects = Project.objects.create(**self.data)
        client.login(username=self.name,password=self.password)
        response = client.put(f'{self.url_project} {projects.id}/', self.data_put)
        # Разобраться, почему тут 415 ошибка:
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        # project_ = Project.objects.get(id=projects.id)
        # self.assertEqual(project_.project, self.data_put.get('test'))
        # self.assertEqual(project_.git_link, self.data_put.get('git.com/proj_1'))

        client.logout()







    def tearDown(self) -> None:
        pass
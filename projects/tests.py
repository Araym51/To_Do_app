from django.test import TestCase
from requests import request
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
import json

from users_app.models import Users
from users_app.views import UsersModelViewSet
from .views import ProjectDjangoFilterViewSet, ToDoDjangoFilterViewSet
from .models import ToDo, Project


# Create your tests here.

class TestProjectViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'araym'
        self.password = 'z1mbabva'
        self.data = {'id': 1, 'project': 'testing', 'git_link': 'https://github.com/', 'is_active': True, }
        self.email = 'adm@ya.ru'
        self.data_put = {'project': 'testing', 'git_link': 'https://github.com/Araym51', 'is_active': False, }
        self.users = {'id': 1, 'username': 'user', 'password': 'pass3124', 'email': 'mail@mail.ru'}
        self.url_project = '/api/project/'
        self.url_users = '/api/users/'
        self.admin = Users.objects.create_superuser(self.name, self.email, self.password)

    def test_project_create_admin(self):
        # создаем админа:
        factory = APIRequestFactory()
        request = factory.post(self.url_users, self.users, format='json')
        force_authenticate(request, self.admin)
        view = UsersModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_project_get_list(self):
        # список проектов:
        factory = APIRequestFactory()
        request = factory.get(self.url_project)
        view = ProjectDjangoFilterViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_get_detail(self):
        # детализация проекта:
        client = APIClient()
        projects = Project.objects.create(**self.data)
        response = client.get(f'{self.url_project} {projects.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_put_object(self):
        client = APIClient()
        projects = Project.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.put(f'{self.url_project}{projects.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

    def test_project_put_mixer(self):
        projects = mixer.blend(Project)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url_project}{projects.id}/', {'git_link': 'https://github.com/Araym51'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        projects_ = Project.objects.get(id=projects.id)
        self.assertEqual(projects_.git_link, 'https://github.com/Araym51')
        self.client.logout()

    def test_project_put_mixer_fields(self):
        projects = mixer.blend(Project)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url_project}{projects.id}/',
                                   {'git_link': 'https://github.com/Araym51', 'is_active': False, })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        projects_ = Project.objects.get(id=projects.id)
        self.assertEqual(projects_.git_link, 'https://github.com/Araym51')
        self.assertEqual(projects_.is_active, False)
        self.client.logout()

    def tearDown(self) -> None:
        pass


class TestToDoViewSet(APITestCase):

    def setUp(self) -> None:
        self.name = 'araym'
        self.password = 'z1mbabva'
        self.email = 'adm@ya.ru'
        self.project_data = {'project': 'testing', 'git_link': 'https://github.com/', 'is_active': True, }
        self.data = {'project': 1, 'note_text': 'some text', 'users': [1], 'is_active': True }
        self.data_put = {'project': 1, 'note_text': 'modified text', 'users': [1], 'is_active': False }
        self.users = {'username': 'user', 'password': 'pass3124', 'email': 'mail@mail.ru'}
        self.url_todo = '/api/todo/'
        self.url_users = '/api/users/'
        self.admin = Users.objects.create_superuser(self.name, self.email, self.password)

    def test_todo_create_admin(self):
        # создаем админа:
        factory = APIRequestFactory()
        request = factory.post(self.url_users, self.users, format='json')
        force_authenticate(request, self.admin)
        view = UsersModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_todo_list(self):
        response = self.client.get(self.url_todo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_get_detail(self):
        client = APIClient()
        todo = mixer.blend(ToDo)
        response = client.get(f'/api/todo/{todo.id}/')
        print(f'test_todo_get_detail: {response}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_put_admin(self):
        user = mixer.blend(Users)
        todo = mixer.blend(ToDo, user=user.id)
        self.client.login(username=self.name, password=self.password)
        put_data =json.dumps({'project': todo.project.id, 'note_text': 'some text', 'users': user.id, 'is_active': False})
        response = self.client.put(f'/api/todo/{todo.id}/', put_data, content_type='application/json')
        print(f'test_todo_put_admin: {response}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()


    def tearDown(self) -> None:
        pass

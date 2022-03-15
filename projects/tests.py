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
        self.email = 'adm@ya.ru'
        self.data = {'id': 1, 'project': 'testing', 'git_link': 'https://github.com/', 'is_active': True, }
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

    def test_project_patch_mixer_fields(self):
        projects = mixer.blend(Project)
        self.client.login(username=self.name, password=self.password)
        response = self.client.patch(f'{self.url_project}{projects.id}/',
                                     {'git_link': 'https://github.com/Araym51', 'is_active': False, },
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        projects_ = Project.objects.get(id=projects.id)
        self.assertEqual(projects_.git_link, 'https://github.com/Araym51')
        self.assertEqual(projects_.is_active, False)
        self.client.logout()

    def test_project_patch_mixer(self):
        project = mixer.blend(Project, project='check!')
        self.client.login(username=self.name, password=self.password)
        response = self.client.patch(f'{self.url_project}{project.id}/', {'git_link': 'https://github.com/Araym51'},
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        projects_ = Project.objects.get(id=project.id)
        self.assertEqual(projects_.git_link, 'https://github.com/Araym51')
        self.client.logout()

    def tearDown(self) -> None:
        pass


class TestToDoViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'araym'
        self.password = 'z1mbabva'
        self.email = 'adm@ya.ru'
        self.users = {'username': 'user', 'password': 'pass3124', 'email': 'mail@mail.ru'}
        self.url_todo = '/api/todo/'
        self.url_users = '/api/users/'
        self.admin = Users.objects.create_superuser(self.name, self.email, self.password)
        self.todo_data = {
            "note_text": "Skill give sometimes foot reduce. Building wonder address listen.",
            "is_active": True,
            "project": 1,
            "users": 1
        }
        self.todo_put = {
            "note_text": "Done here!",
            "is_active": False,
            "project": 1,
            "users": 1
        }

    def test_get_todo_list(self):
        response = self.client.get(self.url_todo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_get_detail(self):
        client = APIClient()
        todo = mixer.blend(ToDo)
        response = client.get(f'/api/todo/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_note(self):
        todo = mixer.blend(ToDo, note_text='check!')
        self.client.login(username=self.name, password=self.password)
        response = self.client.patch(f'{self.url_todo}{todo.id}/', {'note_text': 'suxcess!'},
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo_ = ToDo.objects.get(id=todo.id)
        self.assertEqual(todo_.note_text, 'suxcess!')
        self.client.logout()

    def test_put_note(self):
        data = mixer.blend(ToDo, note_text='Hey!')
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url_todo}{data.id}/', self.todo_put, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_ = ToDo.objects.get(id=data.id)
        self.assertEqual(data_.note_text, "Done here!")
        self.assertEqual(data_.is_active, False)
        self.client.logout()



    def tearDown(self) -> None:
        pass

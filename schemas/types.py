from graphene_django import DjangoObjectType

from projects.models import Project, ToDo
from users_app.models import Users


class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'
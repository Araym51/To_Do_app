from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import ToDo, Project
from users_app.serializers import UsersModelSerializer

class ProjectModelSerializer(ModelSerializer):
    # users = serializers.StringRelatedField(many=True) # !ВКЛЮЧАТЬ КОГДА НЕ НУЖНО РАБОТАТЬ С HTML ФОРМОЙ!
    class Meta:
        model = Project
        fields = '__all__' # ('id', 'project', 'git_link', 'is_active', 'users')
        # read_only_fields = ('users',)


class ToDoModelSerializer(ModelSerializer):
    # project = serializers.StringRelatedField() # !ВКЛЮЧАТЬ КОГДА НЕ НУЖНО РАБОТАТЬ С HTML ФОРМОЙ!
    # users = UsersModelSerializer() # !ВКЛЮЧАТЬ КОГДА НЕ НУЖНО РАБОТАТЬ С HTML ФОРМОЙ!
    class Meta:
        model = ToDo
        fields = '__all__'

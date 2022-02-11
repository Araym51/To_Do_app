from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import ToDo, Project


class ProjectModelSerializer(ModelSerializer):

    # users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ('project', 'git_link', 'users')
        # read_only_fields = ('users',)


class ToDoModelSerializer(ModelSerializer):
    # users = serializers.StringRelatedField(many=True)

    class Meta:
        model = ToDo
        fields = '__all__'

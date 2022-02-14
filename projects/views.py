from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ToDo, Project
from .serializers import ToDoModelSerializer, ProjectModelSerializer
from .pagination import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


# Create your views here.


class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination # 10 записей


class ToDoModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination # 20 записей

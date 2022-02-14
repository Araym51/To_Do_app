from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import ToDo, Project
from .serializers import ToDoModelSerializer, ProjectModelSerializer
from .pagination import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination
from .filters import ProjectFilter, ToDoFilter
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


# Create your views here.


class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination # 10 записей
    # filterset_class = ProjectFilter


class ToDoModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination # 20 записей
    # filterset_class = ToDoFilter


# # фильтрация:
# class ProjectCustomDjangoFilterViewSet(viewsets.ModelViewSet):
#    queryset = Project.objects.all()
#    serializer_class = ProjectModelSerializer
#    filterset_class = ProjectFilter

# class ProjectKwargsFilterView(ListAPIView):
#    serializer_class = ProjectModelSerializer
#
#    def get_queryset(self):
#        # добавить фильтрацию по совпадению части названия проекта
#        project = self.kwargs['project']
#        return Project.objects.filter(name__contains=project)


# class ToDoCustomDjangoFilterViewSet(viewsets.ModelViewSet):
#    queryset = ToDo.objects.all()
#    serializer_class = ToDoModelSerializer
#    filterset_class = ToDoFilter

# class ToDoKwargsFilterView(ListAPIView):
#     serializer_class = ToDoModelSerializer
#
#     def qet_queryset(self):
#         # добавить фильтрацию по проекту
#         project = self.kwargs['project']
#         return ToDo.objects.filter(name__contains=project)


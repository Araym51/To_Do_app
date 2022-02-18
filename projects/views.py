from requests import Response
from rest_framework.viewsets import ModelViewSet
from .models import ToDo, Project
from .serializers import ToDoModelSerializer, ProjectModelSerializer
from .pagination import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination
from .filters import ProjectFilter, ToDoFilter
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import status


# Create your views here.
class ProjectModelViewSet(ModelViewSet):
    """
    доступны все варианты запросов
    """
    # renderer_classes = [BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination # 10 записей


class ToDoModelViewSet(ModelViewSet):
    """
    доступны все варианты запросов;
    при удалении не удалять ToDo, а выставлять признак, что оно закрыто
    """
    # renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination # 20 записей

# фильтрация:
class ProjectDjangoFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    # pagination_class = ProjectLimitOffsetPagination # ! при включении падает отрисовка фронтэндом !


class ToDoDjangoFilterViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_class = ToDoFilter
    # pagination_class = ToDoLimitOffsetPagination # ! при включении падает отрисовка фронтэндом !

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

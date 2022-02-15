from requests import Response
from rest_framework.viewsets import ModelViewSet
from .models import ToDo, Project
from .serializers import ToDoModelSerializer, ProjectModelSerializer
from .pagination import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination
from .filters import ProjectFilter, ToDoFilter
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


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
    pagination_class = ProjectLimitOffsetPagination


class ToDoDjangoFilterViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_class = ToDoFilter
    pagination_class = ToDoLimitOffsetPagination

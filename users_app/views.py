from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Users
from .serializers import UsersModelSerializer, UsersAdminModelSerializer
from .pagination import UsersLimitOffsetPagination
# Create your views here.


class UsersModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer] #формат рендера для наших данных
    queryset = Users.objects.all() # выбираем все объекты из БД Users
    serializer_class = UsersModelSerializer # показываем, каким сериализатором отдаем всё наружу
    pagination_class = UsersLimitOffsetPagination # установлен вывод 10 записей на страницу


class UsersCustomViewSet(ListModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    есть возможность просмотра списка и каждого пользователя в отдельности,
    можно вносить изменения, нельзя удалять и создавать
    """
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Users.objects.all()
    pagination_classes = UsersLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UsersModelSerializer
        return UsersAdminModelSerializer

from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UsersModelSerializer
# Create your views here.


class UsersModelViewSet(ModelViewSet):
    queryset = Users.objects.all() # выбираем все объекты из БД Users
    serializer_class = UsersModelSerializer # показываем, каким сериализатором отдаем всё наружу

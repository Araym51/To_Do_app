from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UsersModelSerializer
# Create your views here.


class UsersModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer] #формат рендера для наших данных
    queryset = Users.objects.all() # выбираем все объекты из БД Users
    serializer_class = UsersModelSerializer # показываем, каким сериализатором отдаем всё наружу

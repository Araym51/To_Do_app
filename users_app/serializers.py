from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Users


class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        # поля которые мы хотим отображать:
        fields = ('username', 'first_name', 'last_name', 'email')
        # fields = '__all__'


class UsersAdminModelSerializer(ModelSerializer):
    """
    1) Создать новую версию API в проекте, в которой у модели пользователя будут доступны поля
    is_superuser, is_staff. Таким образом, проект будет поддерживать две версии API.
    """
    class Meta:
        model = Users
        # поля которые мы хотим отображать:
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')

from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Users


class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        # поля которые мы хотим отображать:
        fields = ('username', 'first_name', 'last_name', 'email')

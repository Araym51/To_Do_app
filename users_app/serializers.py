from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Users


class UsersModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Users
        # поля которые мы хотим отображать:
        fields = ('username', 'first_name', 'last_name', 'email')

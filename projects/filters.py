from django_filters import rest_framework as filters
from .models import ToDo, Project


class ProjectFilter(filters.FilterSet):
   # добавить фильтрацию по совпадению части названия проекта
   """ !!! при активации следующей строки появляется лишнее забагованное поле!!! """
   # name = filters.CharFilter(lookup_expr='contains') # lookup_expr - ищет вхождение, а не строгое равенство

   class Meta:
       model = Project
       fields = ['project'] # todo: разобраться, почему ищет только строгое вхождение



class ToDoFilter(filters.FilterSet):
    # добавить фильтрацию по проекту

    class Meta:
        model = ToDo
        fields = ['project']

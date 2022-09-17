from django_filters import rest_framework as filters
from .models import ToDo, Project


class ProjectFilter(filters.FilterSet):
   # добавить фильтрацию по совпадению части названия проекта
   project = filters.CharFilter(lookup_expr='contains') # lookup_expr - ищет вхождение, а не строгое равенство

   class Meta:
       model = Project
       fields = ['project']


class ToDoFilter(filters.FilterSet):
    # добавить фильтрацию по проекту
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = ToDo
        fields = ['project', 'created_at']

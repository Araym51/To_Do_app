from django_filters import rest_framework as filters
from .models import ToDo, Project


class ProjectFilter(filters.FilterSet):
   name = filters.CharFilter(lookup_expr='contains')

   class Meta:
       model = Project
       fields = ['project']


class ToDoFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = ToDo
        fields = ['project']

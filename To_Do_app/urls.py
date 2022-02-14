"""To_Do_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from users_app.views import UsersModelViewSet
from projects.views import ProjectModelViewSet, ToDoModelViewSet, ProjectDjangoFilterViewSet, ToDoDjangoFilterViewSet


router = DefaultRouter()
# router = SimpleRouter()
router.register('users', UsersModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('to_do', ToDoModelViewSet)
router.register('project_filter', ProjectDjangoFilterViewSet)
router.register('todo_filter', ToDoDjangoFilterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), # подключена админка
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

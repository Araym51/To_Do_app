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
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter, SimpleRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users_app.views import UsersCustomViewSet
from projects.views import ProjectDjangoFilterViewSet, ToDoDjangoFilterViewSet
from rest_framework.authtoken import views

schema_view = get_schema_view(
    openapi.Info(
        title='To do app',
        default_version='1',
        description='Documentation to out project',
        contact=openapi.Contact(email='araimo@yandex.ru'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register('users', UsersCustomViewSet)
router.register('project', ProjectDjangoFilterViewSet)
router.register('todo', ToDoDjangoFilterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # подключена админка
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),  # токен для авторизации
    path('swagger/',schema_view.with_ui('swagger')),
    path('redoc/',schema_view.with_ui('redoc')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]


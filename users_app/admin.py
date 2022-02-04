from django.contrib import admin
from .models import Users
# Register your models here.

"""
регистрируем модель, по которой будет происходить авторизация
"""
admin.site.register(Users)

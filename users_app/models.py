from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser



class Users(AbstractUser):
    """
    по заданию требуется задать поле email как уникальное,
    не забываем в settings добавить AUTH_USER_MODEL = 'users_app.Users'
    а также файл admin.py
    """
    email = models.EmailField(unique=True)

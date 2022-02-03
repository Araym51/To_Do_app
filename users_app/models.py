from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser ,AbstractBaseUser
from django.db import models


class Users(AbstractUser):
    # username = models.CharField(verbose_name='Логин пользователя',max_length=150, unique=True)
    email = models.EmailField(unique=True)

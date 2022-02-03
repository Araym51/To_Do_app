from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Users(AbstractBaseUser):
    email = models.EmailField(verbose_name='e-mail', unique=True, null=False)

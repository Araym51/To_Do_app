from django.db import models

# Create your models here.
import users_app.models


class Project(models.Model):
    project = models.CharField(verbose_name='Название проекта', max_length=128)
    git_link = models.URLField(verbose_name='Ссылка на git')
    users = models.ForeignKey(users_app.models.Users, on_delete=models.CASCADE)


class To_do(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note_text = models.TextField(verbose_name='Описание задачи')
    users = models.ForeignKey(users_app.models.Users, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

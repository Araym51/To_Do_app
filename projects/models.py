from django.db import models

# Create your models here.
from users_app.models import Users

"""
подумать, куда лучше записать created/updated at
"""


class Project(models.Model):
    """
    Добавить модель Project. Это проект, для которого записаны TODO.
    У него есть название, может быть ссылка на репозиторий и набор пользователей, которые работают с этим проектом.
    Создать модель, выбрать подходящие типы полей и связей с другими моделями.
    """
    project = models.CharField(verbose_name='Название проекта', max_length=128)
    git_link = models.URLField(verbose_name='Ссылка на git')
    is_active = models.BooleanField(default=True)
    users = models.ManyToManyField(Users)


class ToDo(models.Model):
    """
    Добавить модель TODO. Это заметка.
    У ToDo есть проект, в котором сделана заметка, текст заметки,
    дата создания и обновления, пользователь, создавший заметку.
    Содержится и признак — активно TODO или закрыто.
    Выбрать подходящие типы полей и связей с другими моделями.
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note_text = models.TextField(verbose_name='Описание заметки')
    users = models.ForeignKey(Users, on_delete=models.PROTECT, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.note_text

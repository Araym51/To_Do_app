from django.db import models

# Create your models here.
import users_app.models

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
    users = models.ManyToManyField(users_app.models.Users)


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
    users = models.ForeignKey(users_app.models.Users, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.project} | {self.note_text} | {self.users} | {self.created_at} | {self.updated_at}'

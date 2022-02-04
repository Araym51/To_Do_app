from users_app.models import Users
from django.core.management.base import BaseCommand
import json


def load_from_json(file_name):
    """
    загружает json айл для чтения
    :param file_name: имя файла для прочтения
    :return: файл в формате json
    """
    with open(file_name, mode='r', encoding='utf-8') as db_file:
        return json.load(db_file)


def user_gen(num):
    """
    Генерирует заданное количество пользователей
    :param num: нужное число пользователей
    :return: возвращается список пользователей
    """
    users_list = []
    while num > 0:
        num -= 1
        data = []
        data.append(f'username{num}')
        data.append(f'user{num}_firstname')
        data.append(f'user{num}_lastname')
        data.append(f'user{num}@mail.ru')
        users_list.append(data)
    return users_list


class Command(BaseCommand):
    def handle(self, *args, **options):
        # создаем суперпользователя:
        Users.objects.create_superuser(username='araym', email='araimo@yandex.ru', password='z1mbabva',
                                       first_name='Egor', last_name='Ostroumov')

        # генерируем список с нужным количеством пользователей
        generated_users = user_gen(20)
        # заполняем базу данных новыми пользователями
        for user_name, first_name, last_name, user_email in generated_users:
            Users.objects.create_user(username=user_name, email=user_email, first_name=first_name, last_name=last_name,
                                      password='zaq12wsx')

        """
        разобраться, почему не добавляются данные при загрузке по скрипту?
        Вероятно проблема в связанности данных
        """
        # users = load_from_json('users_app/fixtures/db.json')
        # Users.objects.all().delete()
        # for user in users:
        #     get_user = user.get('fields')
        #     get_user['id'] = user.get('pk')
        #     new_user = Users(**get_user)
        #     new_user.save()

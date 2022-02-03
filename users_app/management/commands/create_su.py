from users_app.models import Users
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        Users.objects.create_superuser(username='araym', email='araimo@yandex.ru', password='z1mbabva',
                                       first_name='Egor', last_name='Ostroumov')

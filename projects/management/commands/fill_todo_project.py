from mixer.backend.django import mixer
from django.core.management.base import BaseCommand

from projects.models import Project, ToDo


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)


    def handle(self, *args, **options):
        records_count = options['count']
        for i in range(records_count):
            # mixer.blend(Project)
            mixer.blend(ToDo)
        print('ToDo & Project заполнены тестовыми записями')
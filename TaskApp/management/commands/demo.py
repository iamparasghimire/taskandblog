from typing import Any, Optional
from django.core.management.base import BaseCommand
from TaskApp.models import Task

class Command(BaseCommand):
    help = 'create Task for todo app'


    def add_arguments(self, parser):
        parser.add_argument('title',type=str, help = 'title of task')
        parser.add_argument('description',type=str,help='description of task')


    def handle(self, *args, **options):
        title = options['title']
        description = options['description']
        task = Task.objects.create(title = title,description=description) 
        self.stdout.write(self.style.SUCCESS(f'Task "{title}" created with Id {task.id}'))






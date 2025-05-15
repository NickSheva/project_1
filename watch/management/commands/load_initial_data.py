from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Load initial data from fixtures'

    def handle(self, *args, **kwargs):
        if os.path.exists('auth.json'):
            self.stdout.write("Importing auth.json...")
            call_command('loaddata', 'auth.json')
        if os.path.exists('watch.json'):
            self.stdout.write("Importing watch.json...")
            call_command('loaddata', 'watch.json')

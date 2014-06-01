from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run e2e testserver."

    def handle(self, *args, **options):
        #settings.E2E_MODE = True
        call_command('testserver', args[0], interactive = False)


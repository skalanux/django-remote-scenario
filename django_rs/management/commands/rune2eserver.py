#   Remote scenario setup for e2e testing of django projects
#   Copyright (C) 2014  Juan Manuel Schillaci
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
#   django-remote-scneario version 0.1, Copyright (C) 2014  Juan Manuel Schillaci
#   django-remote-scenario comes with ABSOLUTELY NO WARRANTY.
#   This is free software, and you are welcome to redistribute it
#   under certain conditions;
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run e2e testserver."

    def handle(self, *args, **options):
        settings.E2E_MODE = True
        settings.INITIAL_E2E_DATA = args[0]
        call_command('testserver', args[0], interactive=False)


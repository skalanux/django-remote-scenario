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

# This file is loosely based on the testserver django's bundled command

import sys
from optparse import make_option

import django
from django.conf import settings

try:
    from django.contrib.staticfiles.management.commands.runserver import Command as RunServerCommand
except:
    from django.core.management.commands.runserver import Command as RunServerCommand


class Command(RunServerCommand):
    help = "Run patched runserver."

    def inner_run(self, *args, **options):
        # Necessary hack to make reloading work with a test database
        settings.E2E_RELOAD_INITIALIZER()
        super(Command, self).inner_run(*args, **options)

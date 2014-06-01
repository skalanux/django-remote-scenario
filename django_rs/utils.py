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

from django.http import HttpResponse
from django.views.generic import View
from django.core.managment import call_command


class ScenarioView(View):
    def get(self, request):
        """Setup a pristine database with initial data."""
        # Initializes database
        call_command('flush', interactive = False)
        # Loads all initial data fixtures
        call_command('syncdb', interactive = False)

        try:
            self.create_scenario(request)
        except Exception, e:
            return HttpResponse(status=500)
        else:
            return HttpResponse(status=204)

    def create_scenario(self, request):
        raise NotImplementedError

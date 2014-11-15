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
import importlib
import glob
import os

from django.conf import settings
from django.core.management import call_command
from django.http import HttpResponse
from django.shortcuts import render

try:
    E2E_MODE = settings.E2E_MODE
except:
    E2E_MODE = False

def _discover_files(path):
    files = glob.glob(os.path.join(path, "*.py"))
    return [k.split("/")[-1].split(".py")[0] for k in files if k[-11:]!="__init__.py"]


def index(request):
    #Fixme: This entire view needs to be refactorized with proper testing
    # this is just a (Working) proof of concept

    apps = []
    if E2E_MODE:
        for app in settings.INSTALLED_APPS:
            scenarios = []
            mocks = []
            try:
                scenario_module = importlib.import_module(app+".scenarios")
                mocks_module = None
                if hasattr(scenario_module, "mocks"):
                    mocks_module = importlib.import_module(app+".scenarios.mocks")
            except ImportError:
                pass
            else:
                scenarios = _discover_files(scenario_module.__path__[0])
                if mocks_module:
                    mocks = _discover_files(mocks_module.__path__[0])

            if scenarios or mocks:
                apps.append({'name': app, 'scenarios': scenarios, 'mocks': mocks})
    return render(request, "index.html", {'apps': apps})


def scenario(request, app, scenario):
    if E2E_MODE:
        app = app if app in settings.INSTALLED_APPS else None
        if app is None:
            raise ValueError

        imported_scenario = importlib.import_module(app+".scenarios."+scenario)

        flush = request.GET.get('flush', "1")

        flush = True if flush=="1" else False

        if flush:
            # Initializes database
            call_command('flush', interactive=False)
            # Loads all initial data fixtures
            call_command('syncdb', interactive=False)
            call_command('loaddata', *settings.INITIAL_E2E_DATA, interactive = False)

        imported_scenario.main(request)
        # Error
        # return HttpResponse(status=500)
        # OK
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)

def _force_reload():
    """Force django server reloading."""
    # TODO: Touch file
    filename =  "/home/ska/Dropbox/Projects/Devecoop/django-remote-scenario/django_rs/management/commands/rune2eserver.py"
    os.utime(filename, None)

def reset(request):
    import shelve
    di = shelve.open('/tmp/drs_store')
    di.clear()
    di.close()
    _force_reload()
    return HttpResponse(status=200)

def mock(request, app, mock):
    if E2E_MODE:
        app = app if app in settings.INSTALLED_APPS else None
        if app is None:
            raise ValueError

        mock_module_string = str(app+".scenarios.mocks."+mock)

        activate = request.GET.get('activate', '1')

        activate = True if activate=='1' else False

        import shelve
        di = shelve.open('/tmp/drs_store')
        if activate:
           # TODO: Make an ordered list
            di[mock_module_string] = True
        else:
            del di[mock_module_string]
        di.close()
        _force_reload()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)

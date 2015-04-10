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

from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run e2e testserver."
    option_list = BaseCommand.option_list + (
        make_option('--addrport',type='str', dest='addrport',
                    help='port number or ipaddr:port'),
        make_option('--skip-test-db', '-t', action='store_true', dest='skip_test_db', default=False,
                  help='Tells Django to create an ephemeral db.'))

    def handle(self, *fixture_labels, **options):
        from django.core.management import call_command
        from django.db import connection, connections

        settings.E2E_MODE = True
        settings.INITIAL_E2E_DATA = fixture_labels

        verbosity = int(options.get('verbosity'))
        interactive = options.get('interactive')
        addrport = (options.get('addrport', "127.0.0.1:8000"))
        skip_test_db = (options.get('skip_test_db'))

        settings.SKIP_TEST_DB = skip_test_db
        use_threading = connection.features.test_db_allows_multiple_connections

        def load_data():
            call_command('loaddata', *fixture_labels, **{'verbosity': verbosity})

        def initialize_test_db():
            params = {'verbosity': True,
                          'autoclobber': False}

            for connection in connections.all():
                connection.creation.create_test_db(**params)
            load_data()

        def initializer():
            if not settings.SKIP_TEST_DB:
                initialize_test_db()

            import importlib
            import shelve
            di = shelve.open('/tmp/drs_store')
            for mock_module_string, value in di.iteritems():

                imported_mock = importlib.import_module(mock_module_string)

                setattr(imported_mock.to_mock,
                        imported_mock.to_mock_attr,
                        imported_mock.mock
                        )
            di.close()

        settings.MOCKED_MODULES = set()

        if settings.SKIP_TEST_DB:
            load_data()

        settings.E2E_RELOAD_INITIALIZER = initializer

        call_command(
            'runserver_patched',
            addrport=addrport,
            use_reloader=True,
            use_threading=use_threading
            )

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

import sys
import threading
import time

import django
from django.conf import settings
from django.core.management.base import BaseCommand


class SigFinish(Exception):
    pass

def throw_signal_function(frame, event, arg):
    raise SigFinish()

def do_nothing_trace_function(frame, event, arg):
    # Note: each function called will actually call this function
    # so, take care, your program will run slower because of that.
    return None

def interrupt_thread(thread):
    for thread_id, frame in sys._current_frames().items():
        if thread_id == thread.ident:  # Note: Python 2.6 onwards
            set_trace_for_frame_and_parents(frame, throw_signal_function)

def set_trace_for_frame_and_parents(frame, trace_func):
    # Note: this only really works if there's a tracing function set in this
    # thread (i.e.: sys.settrace or threading.settrace must have set the
    # function before)
    while frame:
        if frame.f_trace is None:
            frame.f_trace = trace_func
        frame = frame.f_back
    del frame


class Command(BaseCommand):
    help = "Run e2e testserver."
    option_list = BaseCommand.option_list + (
        make_option('--addrport',type='str', dest='addrport',
                    help='port number or ipaddr:port'),
        make_option('--skip-test-db', '-t', action='store_true', dest='skip_test_db', default=False,
                    help='Tells Django to create an ephemeral db.'))

    def handle(self, *fixture_labels, **options):
        from django.core.management import call_command
        from django.db import connection

        settings.E2E_MODE = True
        settings.INITIAL_E2E_DATA = fixture_labels

        verbosity = int(options.get('verbosity'))
        interactive = options.get('interactive')
        addrport = (options.get('addrport', "127.0.0.1:8000"))
        skip_test_db = (options.get('skip_test_db'))

        interactive = False

        def thread_call_command():
            # Create a test database by default
            settings.SKIP_TEST_DB = skip_test_db
            # Import fixture data into the database.
            use_threading = connection.features.test_db_allows_multiple_connections
            print "use threading %s" % use_threading
            call_command('loaddata', *fixture_labels, **{'verbosity': verbosity})

            call_command(
                'runserver',
                addrport=addrport,
                use_reloader=True,
                use_threading=use_threading
                )

        running = False
        settings.RELOAD_E2E_SERVER = False
        thread_call_command()

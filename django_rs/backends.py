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

# This file is loosely based on django fake auth
# https://github.com/mozilla-services/django-fakeauth/blob/master/django_fakeauth/__init__.py
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User


class FakeBackendAuth(object):
    def authenticate(self, username=None, password=None,
                    bypass=False):
        try:
            user = User.objects.get(id=settings.DEFAULT_FAKE_USER_ID)
        except User.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class FakeMiddlewareAuth(RemoteUserMiddleware):
    def process_request(self, request):
        username, password, bypass = None, None, None

        username = "dummy"
        password = "dummy"
        bypass = True

        user = auth.authenticate(username=username, password=password,
                                    bypass=bypass)
        if user:
            request.user = user
            auth.login(request, user)

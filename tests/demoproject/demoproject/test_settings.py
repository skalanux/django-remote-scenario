from settings import *

SOUTH_TESTS_MIGRATE = False
DATABASES["default"] = {'ENGINE': 'django.db.backends.sqlite3',
                                     'NAME': '/tmp/defaultdb'}

DEFAULT_FAKE_USER_ID = 1
MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
AUTHENTICATION_BACKENDS = ('django_rs.backends.FakeBackendAuth',)
MIDDLEWARE_CLASSES.append('django_rs.backends.FakeMiddlewareAuth')

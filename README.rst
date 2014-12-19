=============================
django-remote-scenario
=============================

.. image:: https://badge.fury.io/py/django-remote-scenario.png
    :target: https://badge.fury.io/py/django-remote-scenario

.. image:: https://travis-ci.org/skalanux/django-remote-scenario.png?branch=master
    :target: https://travis-ci.org/skalanux/django-remote-scenario

.. image:: https://coveralls.io/repos/skalanux/django-remote-scenario/badge.png?branch=master
    :target: https://coveralls.io/r/skalanux/django-remote-scenario?branch=master

Remote scenario setup for e2e testing of django projects

Documentation
-------------

The full documentation will be at https://django-remote-scenario.readthedocs.org.

Quickstart
----------

Install django-remote-scenario::

    pip install django-remote-scenario

Then add it to an existing django project::

    INSTALLED_APPS = [
    ...
    django_rs

Inside your settings file you also need to add the following::

    SETTINGS_FILE_PATH = __file__


You need to add django_rs urls to your project url file like this::

    urlpatterns = patterns('',
    ...
    url(r'^drs/', include('django_rs.urls')),
    ..
    )

To create custom scenarios, just create a directory inside your app named "scenarios"
, then add as many files as scenarioes you want to implement and create a __init__.py
file to import them. Inside each of those files, you need to implement a main() function
setting up the models you want to create for the scenario, you could create them by hand
or use something like django_dynamic_fixtures https://github.com/paulocheque/django-dynamic-fixture

Note: Your scenario is not limited to creating new models, you may also mock specific parts of the enviroment as well


Once everything is ready, start the server this way, this will enable the dynamic call of scenarios::

    python manage.py rune2eserver initial_data.json


Note: You need to pass a initial fixture file with the barebones of your data.

it is also possible (but not mandatory) to pass a specific settings file, for testing purposes,
in case you want to do the tests using a different database for example::

    python manage.py rune2eserver initial_data.json --settings=demoproject.test_settings [fixture1 fixture2....] [--addrport ipaddress:port]

You might also use you existing database to load scenarios on top of it with the "--skip-test-db" or "-t" modifier::


    python manage.py rune2eserver -t initial_data.json


To start using it, just go to the following url::

    http://127.0.0.1:8000/drs/[APPLICATION]/[SCENARIO]

after doing that the database will be populated with the data you provided in your
scenario. Take into account that, everytime you call an scenario, all the other data
in the database is erased, except for the one in your initial_data fixture files, wich
are loaded again, and also the one you pass as a parameter when you call the command.


Inside this repository you will find a demo Django project preconfigured with a simple
scenario that sets up four objects. Use it like this:

First run the server::

    $ python manage.py rune2eserver initial_data.json --settings=demoproject.test_settings

Then go to your browser and setup a scenario::

    http://127.0.0.1:8000/drs/demoapp/scenario_1

You may also pass a parameter to avoid flushing the database on a specific call::

    http://127.0.0.1:8000/drs/demoapp/scenario_1/?flush=0

Later you could see the results on the following url::

    http://127.0.0.1:8000/demoapp/

Experimental scenario listing has been added, and could be checked out by visting the root url for drs (on this case /drs/) ::

    http://127.0.0.1:8000/drs/





Features
--------

* TODO

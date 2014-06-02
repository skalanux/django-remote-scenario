#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_rs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django_rs.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-remote-scenario',
    version=version,
    description="""Remote scenario setup for e2e testing of django projects""",
    long_description=readme + '\n\n' + history,
    author='Juan Manuel Schillaci',
    author_email='jmschillaci@gmail.com',
    url='https://github.com/skalanux/django-remote-scenario',
    packages=[
        'django_rs',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="GPLv3+",
    zip_safe=False,
    keywords='django-remote-scenario',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)

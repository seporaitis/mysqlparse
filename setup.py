#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'pyparsing',
]

test_requirements = [
    'pyparsing',
]

setup(
    name='mysqlparse',
    version='0.1.3',
    description="A library for parsing SQL statements.",
    long_description=readme + '\n\n' + history,
    author="Julius Seporaitis",
    author_email='julius@seporaitis.net',
    url='https://github.com/seporaitis/mysqlparse',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_dir={
        'mysqlparse': 'mysqlparse',
        'mysqlparse.grammar': 'mysqlparse/grammar'
    },
    include_package_data=True,
    install_requires=requirements,
    license="AGPLv3+",
    zip_safe=False,
    keywords='sql parse pyparsing mysql database',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

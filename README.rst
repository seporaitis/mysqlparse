==========
mysqlparse
==========

.. image:: https://img.shields.io/pypi/v/mysqlparse.svg
        :target: https://pypi.python.org/pypi/mysqlparse

.. image:: https://img.shields.io/travis/seporaitis/mysqlparse.svg
        :target: https://travis-ci.org/seporaitis/mysqlparse


A highly experimental attempt to have a sane parser library to parse MySQL statements.

At the moment - use it at your own risk!


Features
--------

* Inconsistently parses SOME SQL strings.


How can you help?
-----------------

Read the generic ``CONTRIBUTORS.rst`` or here's a short personal
sentiment:

This is being built as a potential support for potential dba tools
that we might write at work, so naturally certain things will be
implemented sooner. Currently these are few use-cases we're looking
into:

* Be able to provide suggestions to `ALTER TABLE` statements (e.g.:
  announce when a statement is potentially not backwards compatible
  with code)
* Be able to generate commands for online schema change tools.
* Potentially add some validation support, so that an SQL linting tool
  could be written.


Why?
----

Out of frustration for lack of a better tool.

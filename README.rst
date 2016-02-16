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

* Parses SOME SQL strings.


Example
-------

Some properties that can be accessed.

.. code-block:: python

    >>> from mysqlparse.grammar.sql_file import sql_file_syntax
    >>> sql = sql_file_syntax.parseString("""
    ...     ALTER TABLE `django_user` ADD COLUMN `notes` LONGTEXT NOT NULL
    ... """)
    >>> print(sql.statements[0].statement_type)
    ALTER
    >>> print(sql.statements[0].table_name)
    `django_user`
    >>> print(sql.statements[0].ignore)
    False
    >>> print(sql.statements[0].alter_specification[0].alter_action)
    ADD COLUMN
    >>> print(sql.statements[0].alter_specification[0].column_name)
    `notes`
    >>> print(sql.statements[0].alter_specification[0].data_type)
    LONGTEXT
    >>> print(sql.statements[0].alter_specification[0].null)
    False
    >>> print(sql.statements[0].alter_specification[0].column_position)
    LAST

Checking that the alter statement is backwards compatible with a
previous version of SOME code, which does not know how to save
``notes`` as ``NOT NULL``:

.. code-block:: python

    for statement in sql.statements:
        if statement != 'ALTER':
            continue
        for column in statement.alter_specification:
            if column.data_type == 'LONGTEXT':
                if column.null is False and column.default != 'NULL':
                    print "{s.table_name}.{c.column_name} is `LONGTEXT NOT NULL` which may break the production system. Use `LONGTEXT DEFAULT NULL` instead.".format(
                        s=statement,
                        c=column,
                    )


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

==========
mysqlparse
==========

.. image:: https://img.shields.io/pypi/v/mysqlparse.svg
        :target: https://pypi.python.org/pypi/mysqlparse

.. image:: https://img.shields.io/travis/seporaitis/mysqlparse/master.svg
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

    >>> import mysqlparse
    >>> sql = mysqlparse.parse("""
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

A short list of things that would help (from relatively easiest):

* Raise an issue with an edge case statement that **should** parse,
  but doesn't.

* Raise an issue with how you would like to use this library.

* Document the available properties in the parsed object.

* Add a missing test case or suggest a way to avoid so much repetition
  in tests checking the same statement, but with variations.

* Suggest how to use ``pyparsing`` to do statement validation.

* Maybe it is possible to generate ``pyparsing`` parser from the MySQL
  source code?

* Add ability to unparse the parse (sub)trees back into valid SQL.


Why?
----

Out of frustration for lack of a better tool.

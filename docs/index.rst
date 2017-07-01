.. mysqlparse documentation master file, created by
   sphinx-quickstart on Sat Feb 27 16:25:51 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mysqlparse documentation
======================================

The purpose of ``mysqlparse`` library is to provide structural access
to MySQL queries. It looks better with an example:

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


Contents
--------

.. toctree::
   :maxdepth: 1

   installation
   statements
   structure

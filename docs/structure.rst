Statements Structure
====================

``mysqlparse.parse(file_or_string)``
------------------------------------

Takes a file like object or string and returns
``pyparsing.ParseResults`` representing the SQL file structure.

Assuming sql file is parsed like this:

.. code-block:: python

   >>> with open('001_migrate.sql') as sql_file:
   >>>     sql = mysqlparse.parse(sql_file)

The following properties are accessible

* ``sql.statements[] : list`` all individual sql statements, separated
  by ``;`` are accessible through this list.

  * ``.statement_type : str``, currently only ``ALTER``.
  * ``.database_name : str``, ``None`` or database
    name if the table identifier was with a dot
    (e.g. ``db_name.tbl_name``).
  * ``.table_name : str``, table name of ``ALTER
    TABLE`` statement.
  * ``.ignore : boolean``, ``True`` if it is ``ALTER
    IGNORE TABLE`` statement (support for it is removed as of MySQL
    5.7.4).
  * ``.alter_specification[] : list`` list of individual
    column alterations.

    * ``.alter_action : str`` one of:

      * ``ADD COLUMN``
      * ``ADD INDEX``
      * ``MODIFY COLUMN``
      * ``CHANGE COLUMN``
      * ``DROP COLUMN``
      * ``DROP PRIMARY KEY``
      * ``DROP INDEX``
      * ``DROP KEY``
      * ``DROP FOREIGN KEY``.

    * ``.column_name : str``
    * ``.new_column_name : str`` name of the new column name in ``MODIFY COLUMN`` statements.
    * ``.null : boolean|str`` - ``True`` if the column is null, ``False`` - if not null and ``implicit`` if unspecified.
    * ``.default : str`` - default value of the column.
    * ``.auto_increment : boolean`` - ``True`` if the column is auto increment.
    * ``.index_type : str`` - ``unique_key`` if column is unique key,
      ``.primary_key`` if column is primary key, ``BTREE`` if it is
      btree, ``HASH`` if it is has.
    * ``.key_block_size : str`` key block size of index.
    * ``.parser_name : str`` name of the parser.
    * ``.comment : str`` - comment string.
    * ``.column_position : str`` one of: ``FIRST``, another column
      name or (default) ``LAST``.
    * ``.data_type : str`` one of:

      * ``BIT``
      * ``TINYINT``
      * ``SMALLINT``
      * ``MEDIUMINT``
      * ``INT``
      * ``INTEGER``
      * ``BIGINT``
      * ``REAL``
      * ``DOUBLE``
      * ``FLOAT``
      * ``DECIMAL``
      * ``NUMERIC``
      * ``DATE``
      * ``TIME``
      * ``TIMESTAMP``
      * ``DATETIME``
      * ``YEAR``
      * ``CHAR``
      * ``VARCHAR``
      * ``BINARY``
      * ``VARBINARY``
      * ``TINYBLOB``
      * ``BLOB``
      * ``MEDIUMBLOB``
      * ``LONGBLOB``
      * ``TINYTEXT``
      * ``TEXT``
      * ``MEDIUMTEXT``
      * ``LONGTEXT``
      * ``ENUM``
      * ``SET``

    * ``.length : str`` - column length (as in ``INT(length)``).
    * ``.decimals : str`` - number of decimal places of a decimal type.
    * ``.unsigned : boolean`` - ``True`` if column is of ``UNSIGNED`` type.
    * ``.zerofill : boolean`` - ``True`` if column is of ``ZEROFILL`` type.
    * ``.binary : boolean`` - ``True`` if column is of ``BINARY`` type.
    * ``.character_set : str`` - character set of the column.
    * ``.collate : str`` - column collation name.

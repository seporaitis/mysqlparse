Supported Statements
====================

This is how ``mysqlparse`` coverage compares to `MySQL ALTER TABLE`_
statement syntax:

.. code-block:: sql

   ALTER TABLE tbl_name
       [alter_specification [, alter_specification] ...]

   alter_specification:
       ADD [COLUMN] col_name column_definition
           [FIRST | AFTER col_name]
     | ADD {INDEX | KEY} [index_name]
           [index_type] (index_col_name, ...) [index_option] ...
     | CHANGE [COLUMN] old_col_name new_col_name column_definition
           [FIRST | AFTER col_name]
     | MODIFY [COLUMN] col_name column_definition
           [FIRST | AFTER col_name]
     | DROP [COLUMN] col_name
     | DROP PRIMARY KEY
     | DROP {INDEX | KEY} index_name
     | DROP FOREIGN KEY fk_symbol

   index_type:
       USING {BTREE | HASH}

   index_option:
       KEY_BLOCK_SIZE [=] value
     | index_type
     | WITH PARSER parser_name
     | COMMENT 'string'

.. _`MySQL ALTER TABLE`: http://dev.mysql.com/doc/refman/5.7/en/alter-table.html

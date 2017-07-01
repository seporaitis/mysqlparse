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

   column_definition:
       data_type [NOT NULL | NULL] [DEFAULT default_value]
       [AUTO_INCREMENT] [UNIQUE [KEY] | [PRIMARY] KEY]
       [COMMENT 'string']

   data_type:
       BIT[(length)]
     | TINYINT[(length)] [UNSIGNED] [ZEROFILL]
     | SMALLINT[(length)] [UNSIGNED] [ZEROFILL]
     | MEDIUMINT[(length)] [UNSIGNED] [ZEROFILL]
     | INT[(length)] [UNSIGNED] [ZEROFILL]
     | INTEGER[(length)] [UNSIGNED] [ZEROFILL]
     | BIGINT[(length)] [UNSIGNED] [ZEROFILL]
     | REAL[(length,decimals)] [UNSIGNED] [ZEROFILL]
     | DOUBLE[(length,decimals)] [UNSIGNED] [ZEROFILL]
     | FLOAT[(length,decimals)] [UNSIGNED] [ZEROFILL]
     | DECIMAL[(length[,decimals])] [UNSIGNED] [ZEROFILL]
     | NUMERIC[(length[,decimals])] [UNSIGNED] [ZEROFILL]
     | DATE
     | TIME[(fsp)]
     | TIMESTAMP[(fsp)]
     | DATETIME[(fsp)]
     | YEAR
     | CHAR[(length)] [BINARY]
         [CHARACTER SET charset_name] [COLLATE collation_name]
     | VARCHAR(length) [BINARY]
         [CHARACTER SET charset_name] [COLLATE collation_name]
     | BINARY[(length)]
     | VARBINARY(length)
     | TINYBLOB
     | BLOB
     | MEDIUMBLOB
     | LONGBLOB
     | TINYTEXT [BINARY]
         [CHARACTER SET charset_name] [COLLATE collation_name]
     | TEXT [BINARY]
         [CHARACTER SET charset_name] [COLLATE collation_name]
     | MEDIUMTEXT [BINARY]
         [CHARACTER SET charset_name] [COLLATE collation_name]
     | LONGTEXT [BINARY]
         [CHARACTER SET charset_name] [COLLATE collation_name]
     | ENUM(value1,value2,value3,...)
         [CHARACTER SET charset_name] [COLLATE collation_name]
     | SET(value1,value2,value3,...)
         [CHARACTER SET charset_name] [COLLATE collation_name]

.. _`MySQL ALTER TABLE`: http://dev.mysql.com/doc/refman/5.7/en/alter-table.html

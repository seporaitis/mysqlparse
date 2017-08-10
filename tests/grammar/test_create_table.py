# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from mysqlparse.grammar.create_table import create_table_syntax


class CreateTableSyntaxTest(unittest.TestCase):

    def test_create_table(self):
        statement = create_table_syntax.parseString("""
        CREATE TABLE test_test (
          id INT(11) PRIMARY KEY,
          col_no1 VARCHAR(255) NOT NULL
        );
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertFalse(statement.temporary)
        self.assertTrue(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.column_specification[0].column_name, "id")
        self.assertEqual(statement.column_specification[1].column_name, "col_no1")
        self.assertEqual(len(statement.table_options), 0)

    def test_create_table_with_options(self):
        statement = create_table_syntax.parseString("""
        CREATE TABLE test_test (
          id INT(11) PRIMARY KEY,
          col_no1 VARCHAR(255) NOT NULL
        ) ENGINE=MyISAM AUTO_INCREMENT id;
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertFalse(statement.temporary)
        self.assertTrue(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.column_specification[0].column_name, "id")
        self.assertEqual(statement.column_specification[1].column_name, "col_no1")
        self.assertEqual(len(statement.table_options), 2)
        self.assertEqual(statement.table_options[0].key, 'ENGINE')
        self.assertEqual(statement.table_options[0].value, 'MyISAM')
        self.assertEqual(statement.table_options[1].key, 'AUTO_INCREMENT')
        self.assertEqual(statement.table_options[1].value, 'id')

    def test_create_temporary_table(self):
        statement = create_table_syntax.parseString("""
        CREATE TEMPORARY TABLE test_test (
          id INT(11) PRIMARY KEY,
          col_no1 VARCHAR(255) NOT NULL
        ) ENGINE=MyISAM AUTO_INCREMENT id;
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertTrue(statement.temporary)
        self.assertTrue(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.column_specification[0].column_name, "id")
        self.assertEqual(statement.column_specification[1].column_name, "col_no1")
        self.assertEqual(statement.table_options[0].key, 'ENGINE')
        self.assertEqual(statement.table_options[0].value, 'MyISAM')
        self.assertEqual(statement.table_options[1].key, 'AUTO_INCREMENT')
        self.assertEqual(statement.table_options[1].value, 'id')

    def test_create_table_overwrite(self):
        statement = create_table_syntax.parseString("""
        CREATE TABLE IF NOT EXISTS test_test (
          id INT(11) PRIMARY KEY,
          col_no1 VARCHAR(255) NOT NULL
        ) ENGINE=MyISAM AUTO_INCREMENT id;
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertFalse(statement.temporary)
        self.assertFalse(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.column_specification[0].column_name, "id")
        self.assertEqual(statement.column_specification[1].column_name, "col_no1")
        self.assertEqual(statement.table_options[0].key, 'ENGINE')
        self.assertEqual(statement.table_options[0].value, 'MyISAM')
        self.assertEqual(statement.table_options[1].key, 'AUTO_INCREMENT')
        self.assertEqual(statement.table_options[1].value, 'id')

    def test_create_temporary_table_overwrite(self):
        statement = create_table_syntax.parseString("""
        CREATE TEMPORARY TABLE IF NOT EXISTS test_test (
          id INT(11) PRIMARY KEY,
          col_no1 VARCHAR(255) NOT NULL
        ) ENGINE=MyISAM AUTO_INCREMENT id;
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertTrue(statement.temporary)
        self.assertFalse(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.column_specification[0].column_name, "id")
        self.assertEqual(statement.column_specification[1].column_name, "col_no1")
        self.assertEqual(statement.table_options[0].key, 'ENGINE')
        self.assertEqual(statement.table_options[0].value, 'MyISAM')
        self.assertEqual(statement.table_options[1].key, 'AUTO_INCREMENT')
        self.assertEqual(statement.table_options[1].value, 'id')

    def test_create_constraint(self):
        statement = create_table_syntax.parseString("""
        CREATE TABLE test_test (
          id INT(11),
          col_no1 VARCHAR(255) NOT NULL,
          CONSTRAINT pkey PRIMARY KEY
        ) ENGINE=MyISAM AUTO_INCREMENT id;
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertFalse(statement.temporary)
        self.assertTrue(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')

        self.assertEqual(statement.column_specification[0].column_name, "id")
        self.assertEqual(statement.column_specification[1].column_name, "col_no1")
        self.assertEqual(statement.constraints[0].symbol, 'pkey')
        self.assertEqual(statement.constraints[0].index_type, False)

    def test_create_constraint_with_index_type(self):
        statement = create_table_syntax.parseString("""
        CREATE TABLE test_test (
          id INT(11),
          col_no1 VARCHAR(255) NOT NULL,
          CONSTRAINT pkey PRIMARY KEY USING BTREE
        ) ENGINE=MyISAM AUTO_INCREMENT id;
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertFalse(statement.temporary)
        self.assertTrue(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')

        self.assertEqual(statement.column_specification[0].column_name, "id")
        self.assertEqual(statement.column_specification[1].column_name, "col_no1")
        self.assertEqual(statement.constraints[0].symbol, 'pkey')
        self.assertEqual(statement.constraints[0].index_type, 'BTREE')

    def test_create_constraint_with_index_type_with_index_columns(self):
        statement = create_table_syntax.parseString("""
        CREATE TABLE test_test (
          id INT(11),
          col_no1 VARCHAR(255) NOT NULL,
          CONSTRAINT pkey PRIMARY KEY USING BTREE (id, col_no1(16))
        ) ENGINE=MyISAM AUTO_INCREMENT id;
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertFalse(statement.temporary)
        self.assertTrue(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')

        self.assertEqual(statement.column_specification[0].column_name, "id")
        self.assertEqual(statement.column_specification[1].column_name, "col_no1")
        self.assertEqual(statement.constraints[0].symbol, 'pkey')
        self.assertEqual(statement.constraints[0].index_type, 'BTREE')
        self.assertEqual(statement.constraints[0].index_columns[0].column_name, 'id')
        self.assertFalse(statement.constraints[0].index_columns[0].length)
        self.assertEqual(statement.constraints[0].index_columns[1].column_name, 'col_no1')
        self.assertEqual(statement.constraints[0].index_columns[1].length, 16)

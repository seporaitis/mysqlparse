# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from mysqlparse.grammar.alter_table import alter_table_syntax


class AlterTableSyntaxTest(unittest.TestCase):

    def test_alter_table_add(self):
        statement = alter_table_syntax.parseString("""
        ALTER IGNORE TABLE test_test ADD col_no0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD col_no1 LONGTEXT NOT NULL,
            ADD col_no2 VARCHAR(200) NULL,
            ADD col_no3 BIT(8) AFTER col0;
        """)

        self.assertTrue(statement.ignore)
        self.assertEquals(statement.statement_type, 'ALTER')
        self.assertEquals(statement.table_name, 'test_test')
        self.assertEquals(statement.alter_specification[0].column_name, 'col_no0')
        self.assertEquals(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEquals(statement.alter_specification[1].column_name, 'col_no1')
        self.assertEquals(statement.alter_specification[1].column_position, 'LAST')
        self.assertEquals(statement.alter_specification[2].column_name, 'col_no2')
        self.assertEquals(statement.alter_specification[2].column_position, 'LAST')
        self.assertEquals(statement.alter_specification[3].column_name, 'col_no3')
        self.assertEquals(statement.alter_specification[3].column_position, 'col0')

    def test_alter_table_add_column(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test ADD COLUMN col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD COLUMN col1 LONGTEXT NOT NULL,
            ADD COLUMN col2 VARCHAR(200) NULL,
            ADD COLUMN col3 BIT(8) AFTER col0;
        """)

        self.assertFalse(statement.ignore)
        self.assertEquals(statement.statement_type, 'ALTER')
        self.assertEquals(statement.table_name, 'test_test')
        self.assertEquals(statement.alter_specification[0].column_name, 'col0')
        self.assertEquals(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEquals(statement.alter_specification[1].column_name, 'col1')
        self.assertEquals(statement.alter_specification[1].column_position, 'LAST')
        self.assertEquals(statement.alter_specification[2].column_name, 'col2')
        self.assertEquals(statement.alter_specification[2].column_position, 'LAST')
        self.assertEquals(statement.alter_specification[3].column_name, 'col3')
        self.assertEquals(statement.alter_specification[3].column_position, 'col0')

    def test_alter_table_add_column_mixed(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test ADD col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD COLUMN col1 LONGTEXT NOT NULL,
            ADD COLUMN col2 VARCHAR(200) NULL,
            ADD col3 BIT(8) AFTER col0;
        """)

        self.assertFalse(statement.ignore)
        self.assertEquals(statement.statement_type, 'ALTER')
        self.assertEquals(statement.table_name, 'test_test')
        self.assertEquals(statement.alter_specification[0].column_name, 'col0')
        self.assertEquals(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEquals(statement.alter_specification[1].column_name, 'col1')
        self.assertEquals(statement.alter_specification[1].column_position, 'LAST')
        self.assertEquals(statement.alter_specification[2].column_name, 'col2')
        self.assertEquals(statement.alter_specification[2].column_position, 'LAST')
        self.assertEquals(statement.alter_specification[3].column_name, 'col3')
        self.assertEquals(statement.alter_specification[3].column_position, 'col0')

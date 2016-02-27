# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from mysqlparse.grammar.alter_table import alter_table_syntax


class AlterTableAddColumnSyntaxTest(unittest.TestCase):

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


class AlterTableAddIndexSyntaxTest(unittest.TestCase):

    def test_alter_table_add_index(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test ADD col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD INDEX index1 (col0, col1 (10), col2 (20) DESC);
        """)

        self.assertFalse(statement.ignore)
        self.assertEquals(statement.statement_type, 'ALTER')
        self.assertEquals(statement.table_name, 'test_test')
        self.assertEquals(statement.alter_specification[0].column_name, 'col0')
        self.assertEquals(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEquals(statement.alter_specification[1].alter_action, 'ADD INDEX')
        self.assertEquals(statement.alter_specification[1].index_name, 'index1')
        self.assertFalse(statement.alter_specification[1].index_type)
        self.assertEquals(statement.alter_specification[1].index_columns[0].column_name, 'col0')
        self.assertFalse(statement.alter_specification[1].index_columns[0].length)
        self.assertFalse(statement.alter_specification[1].index_columns[0].direction)
        self.assertEquals(statement.alter_specification[1].index_columns[1].column_name, 'col1')
        self.assertEquals(statement.alter_specification[1].index_columns[1].length[0], '10')
        self.assertFalse(statement.alter_specification[1].index_columns[1].direction)
        self.assertEquals(statement.alter_specification[1].index_columns[2].column_name, 'col2')
        self.assertEquals(statement.alter_specification[1].index_columns[2].length[0], '20')
        self.assertEquals(statement.alter_specification[1].index_columns[2].direction, 'DESC')

    def test_alter_table_add_index_index_type(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test ADD col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD INDEX index1 USING BTREE (col0, col1 (10), col2 (20) DESC);
        """)

        self.assertFalse(statement.ignore)
        self.assertEquals(statement.statement_type, 'ALTER')
        self.assertEquals(statement.table_name, 'test_test')
        self.assertEquals(statement.alter_specification[0].column_name, 'col0')
        self.assertEquals(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEquals(statement.alter_specification[1].alter_action, 'ADD INDEX')
        self.assertEquals(statement.alter_specification[1].index_name, 'index1')
        self.assertFalse(statement.alter_specification[1].index_type)
        self.assertEquals(statement.alter_specification[1].index_columns[0].column_name, 'col0')
        self.assertFalse(statement.alter_specification[1].index_columns[0].length)
        self.assertFalse(statement.alter_specification[1].index_columns[0].direction)
        self.assertEquals(statement.alter_specification[1].index_columns[1].column_name, 'col1')
        self.assertEquals(statement.alter_specification[1].index_columns[1].length[0], '10')
        self.assertFalse(statement.alter_specification[1].index_columns[1].direction)
        self.assertEquals(statement.alter_specification[1].index_columns[2].column_name, 'col2')
        self.assertEquals(statement.alter_specification[1].index_columns[2].length[0], '20')
        self.assertEquals(statement.alter_specification[1].index_columns[2].direction, 'DESC')

    def test_alter_table_add_index_index_option(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test ADD col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD INDEX index1 (col0, col1 (10), col2 (20) DESC)
                      KEY_BLOCK_SIZE=256
                      USING HASH
                      WITH PARSER some_parser
                      COMMENT 'test comment';
        """)

        self.assertFalse(statement.ignore)
        self.assertEquals(statement.statement_type, 'ALTER')
        self.assertEquals(statement.table_name, 'test_test')
        self.assertEquals(statement.alter_specification[0].column_name, 'col0')
        self.assertEquals(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEquals(statement.alter_specification[1].alter_action, 'ADD INDEX')
        self.assertEquals(statement.alter_specification[1].index_name, 'index1')
        self.assertEquals(statement.alter_specification[1].index_type[0], 'HASH')
        self.assertEquals(statement.alter_specification[1].index_columns[0].column_name, 'col0')
        self.assertFalse(statement.alter_specification[1].index_columns[0].length)
        self.assertFalse(statement.alter_specification[1].index_columns[0].direction)
        self.assertEquals(statement.alter_specification[1].index_columns[1].column_name, 'col1')
        self.assertEquals(statement.alter_specification[1].index_columns[1].length[0], '10')
        self.assertFalse(statement.alter_specification[1].index_columns[1].direction)
        self.assertEquals(statement.alter_specification[1].index_columns[2].column_name, 'col2')
        self.assertEquals(statement.alter_specification[1].index_columns[2].length[0], '20')
        self.assertEquals(statement.alter_specification[1].index_columns[2].direction, 'DESC')
        self.assertEquals(statement.alter_specification[1].key_block_size[0], '256')
        self.assertEquals(statement.alter_specification[1].parser_name[0], 'some_parser')
        self.assertEquals(statement.alter_specification[1].comment[0], 'test comment')


class AlterTableModifyColumnSyntaxTest(unittest.TestCase):

    def test_alter_table_modify(self):
        statement = alter_table_syntax.parseString("""
        ALTER IGNORE TABLE test_test MODIFY col_no0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            MODIFY col_no1 LONGTEXT NOT NULL,
            MODIFY col_no2 VARCHAR(200) NULL,
            MODIFY col_no3 BIT(8) AFTER col0;
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

    def test_alter_table_modify_column(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test MODIFY COLUMN col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            MODIFY COLUMN col1 LONGTEXT NOT NULL,
            MODIFY COLUMN col2 VARCHAR(200) NULL,
            MODIFY COLUMN col3 BIT(8) AFTER col0;
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

    def test_alter_table_modify_column_mixed(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test MODIFY col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            MODIFY COLUMN col1 LONGTEXT NOT NULL,
            MODIFY COLUMN col2 VARCHAR(200) NULL,
            MODIFY col3 BIT(8) AFTER col0;
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

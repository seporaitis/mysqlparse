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
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col_no0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].column_name, 'col_no1')
        self.assertEqual(statement.alter_specification[1].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[2].column_name, 'col_no2')
        self.assertEqual(statement.alter_specification[2].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[3].column_name, 'col_no3')
        self.assertEqual(statement.alter_specification[3].column_position, 'col0')

    def test_alter_table_add_column(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test ADD COLUMN col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD COLUMN col1 LONGTEXT NOT NULL,
            ADD COLUMN col2 VARCHAR(200) NULL,
            ADD COLUMN col3 BIT(8) AFTER col0;
        """)

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].column_name, 'col1')
        self.assertEqual(statement.alter_specification[1].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[2].column_name, 'col2')
        self.assertEqual(statement.alter_specification[2].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[3].column_name, 'col3')
        self.assertEqual(statement.alter_specification[3].column_position, 'col0')

    def test_alter_table_add_column_mixed(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test ADD col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD COLUMN col1 LONGTEXT NOT NULL,
            ADD COLUMN col2 VARCHAR(200) NULL,
            ADD col3 BIT(8) AFTER col0;
        """)

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].column_name, 'col1')
        self.assertEqual(statement.alter_specification[1].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[2].column_name, 'col2')
        self.assertEqual(statement.alter_specification[2].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[3].column_name, 'col3')
        self.assertEqual(statement.alter_specification[3].column_position, 'col0')


class AlterTableAddIndexSyntaxTest(unittest.TestCase):

    def test_alter_table_add_index(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test ADD col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD INDEX index1 (col0, col1 (10), col2 (20) DESC);
        """)

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].alter_action, 'ADD INDEX')
        self.assertEqual(statement.alter_specification[1].index_name, 'index1')
        self.assertFalse(statement.alter_specification[1].index_type)
        self.assertEqual(statement.alter_specification[1].index_columns[0].column_name, 'col0')
        self.assertFalse(statement.alter_specification[1].index_columns[0].length)
        self.assertFalse(statement.alter_specification[1].index_columns[0].direction)
        self.assertEqual(statement.alter_specification[1].index_columns[1].column_name, 'col1')
        self.assertEqual(statement.alter_specification[1].index_columns[1].length[0], '10')
        self.assertFalse(statement.alter_specification[1].index_columns[1].direction)
        self.assertEqual(statement.alter_specification[1].index_columns[2].column_name, 'col2')
        self.assertEqual(statement.alter_specification[1].index_columns[2].length[0], '20')
        self.assertEqual(statement.alter_specification[1].index_columns[2].direction, 'DESC')

    def test_alter_table_add_index_index_type(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test ADD col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD INDEX index1 USING BTREE (col0, col1 (10), col2 (20) DESC);
        """)

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].alter_action, 'ADD INDEX')
        self.assertEqual(statement.alter_specification[1].index_name, 'index1')
        self.assertFalse(statement.alter_specification[1].index_type)
        self.assertEqual(statement.alter_specification[1].index_columns[0].column_name, 'col0')
        self.assertFalse(statement.alter_specification[1].index_columns[0].length)
        self.assertFalse(statement.alter_specification[1].index_columns[0].direction)
        self.assertEqual(statement.alter_specification[1].index_columns[1].column_name, 'col1')
        self.assertEqual(statement.alter_specification[1].index_columns[1].length[0], '10')
        self.assertFalse(statement.alter_specification[1].index_columns[1].direction)
        self.assertEqual(statement.alter_specification[1].index_columns[2].column_name, 'col2')
        self.assertEqual(statement.alter_specification[1].index_columns[2].length[0], '20')
        self.assertEqual(statement.alter_specification[1].index_columns[2].direction, 'DESC')

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
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].alter_action, 'ADD INDEX')
        self.assertEqual(statement.alter_specification[1].index_name, 'index1')
        self.assertEqual(statement.alter_specification[1].index_type[0], 'HASH')
        self.assertEqual(statement.alter_specification[1].index_columns[0].column_name, 'col0')
        self.assertFalse(statement.alter_specification[1].index_columns[0].length)
        self.assertFalse(statement.alter_specification[1].index_columns[0].direction)
        self.assertEqual(statement.alter_specification[1].index_columns[1].column_name, 'col1')
        self.assertEqual(statement.alter_specification[1].index_columns[1].length[0], '10')
        self.assertFalse(statement.alter_specification[1].index_columns[1].direction)
        self.assertEqual(statement.alter_specification[1].index_columns[2].column_name, 'col2')
        self.assertEqual(statement.alter_specification[1].index_columns[2].length[0], '20')
        self.assertEqual(statement.alter_specification[1].index_columns[2].direction, 'DESC')
        self.assertEqual(statement.alter_specification[1].key_block_size[0], '256')
        self.assertEqual(statement.alter_specification[1].parser_name[0], 'some_parser')
        self.assertEqual(statement.alter_specification[1].comment[0], 'test comment')


class AlterTableModifyColumnSyntaxTest(unittest.TestCase):

    def test_alter_table_modify(self):
        statement = alter_table_syntax.parseString("""
        ALTER IGNORE TABLE test_test MODIFY col_no0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            MODIFY col_no1 LONGTEXT NOT NULL,
            MODIFY col_no2 VARCHAR(200) NULL,
            MODIFY col_no3 BIT(8) AFTER col0;
        """)

        self.assertTrue(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col_no0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].column_name, 'col_no1')
        self.assertEqual(statement.alter_specification[1].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[2].column_name, 'col_no2')
        self.assertEqual(statement.alter_specification[2].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[3].column_name, 'col_no3')
        self.assertEqual(statement.alter_specification[3].column_position, 'col0')

    def test_alter_table_modify_column(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test MODIFY COLUMN col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            MODIFY COLUMN col1 LONGTEXT NOT NULL,
            MODIFY COLUMN col2 VARCHAR(200) NULL,
            MODIFY COLUMN col3 BIT(8) AFTER col0;
        """)

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].column_name, 'col1')
        self.assertEqual(statement.alter_specification[1].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[2].column_name, 'col2')
        self.assertEqual(statement.alter_specification[2].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[3].column_name, 'col3')
        self.assertEqual(statement.alter_specification[3].column_position, 'col0')

    def test_alter_table_modify_column_mixed(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test MODIFY col0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            MODIFY COLUMN col1 LONGTEXT NOT NULL,
            MODIFY COLUMN col2 VARCHAR(200) NULL,
            MODIFY col3 BIT(8) AFTER col0;
        """)

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].column_name, 'col1')
        self.assertEqual(statement.alter_specification[1].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[2].column_name, 'col2')
        self.assertEqual(statement.alter_specification[2].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[3].column_name, 'col3')
        self.assertEqual(statement.alter_specification[3].column_position, 'col0')


class AlterTableChangeColumnSyntaxTest(unittest.TestCase):

    def test_alter_table_change(self):
        statement = alter_table_syntax.parseString("""
        ALTER IGNORE TABLE test_test CHANGE col_no0 col_0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            CHANGE col_no1 col_1 LONGTEXT NOT NULL,
            CHANGE col_no2 col_2 VARCHAR(200) NULL,
            CHANGE col_no3 col_3 BIT(8) AFTER col0;
        """)

        self.assertTrue(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col_no0')
        self.assertEqual(statement.alter_specification[0].new_column_name, 'col_0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].column_name, 'col_no1')
        self.assertEqual(statement.alter_specification[1].new_column_name, 'col_1')
        self.assertEqual(statement.alter_specification[1].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[2].column_name, 'col_no2')
        self.assertEqual(statement.alter_specification[2].new_column_name, 'col_2')
        self.assertEqual(statement.alter_specification[2].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[3].column_name, 'col_no3')
        self.assertEqual(statement.alter_specification[3].new_column_name, 'col_3')
        self.assertEqual(statement.alter_specification[3].column_position, 'col0')

    def test_alter_table_change_column(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test CHANGE COLUMN col0 col_no0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            CHANGE COLUMN col1 col_no1 LONGTEXT NOT NULL,
            CHANGE COLUMN col2 col_no2 VARCHAR(200) NULL,
            CHANGE COLUMN col3 col_no3 BIT(8) AFTER col0;
        """)

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col0')
        self.assertEqual(statement.alter_specification[0].new_column_name, 'col_no0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].column_name, 'col1')
        self.assertEqual(statement.alter_specification[1].new_column_name, 'col_no1')
        self.assertEqual(statement.alter_specification[1].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[2].column_name, 'col2')
        self.assertEqual(statement.alter_specification[2].new_column_name, 'col_no2')
        self.assertEqual(statement.alter_specification[2].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[3].column_name, 'col3')
        self.assertEqual(statement.alter_specification[3].new_column_name, 'col_no3')
        self.assertEqual(statement.alter_specification[3].column_position, 'col0')

    def test_alter_table_change_column_mixed(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test CHANGE col0 col_no0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            CHANGE COLUMN col1 col_no1 LONGTEXT NOT NULL,
            CHANGE COLUMN col2 col_no2 VARCHAR(200) NULL,
            CHANGE col3 col_no3 BIT(8) AFTER col0;
        """)

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].column_name, 'col0')
        self.assertEqual(statement.alter_specification[0].new_column_name, 'col_no0')
        self.assertEqual(statement.alter_specification[0].column_position, 'FIRST')
        self.assertEqual(statement.alter_specification[1].column_name, 'col1')
        self.assertEqual(statement.alter_specification[1].new_column_name, 'col_no1')
        self.assertEqual(statement.alter_specification[1].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[2].column_name, 'col2')
        self.assertEqual(statement.alter_specification[2].new_column_name, 'col_no2')
        self.assertEqual(statement.alter_specification[2].column_position, 'LAST')
        self.assertEqual(statement.alter_specification[3].column_name, 'col3')
        self.assertEqual(statement.alter_specification[3].new_column_name, 'col_no3')
        self.assertEqual(statement.alter_specification[3].column_position, 'col0')


class AlterTableDropSyntaxTest(unittest.TestCase):

    def test_drop(self):
        statement = alter_table_syntax.parseString(
            "ALTER TABLE test_test DROP col_no0;"
        )

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].alter_action, 'DROP COLUMN')
        self.assertEqual(statement.alter_specification[0].column_name, 'col_no0')

    def test_drop_column(self):
        statement = alter_table_syntax.parseString(
            "ALTER TABLE test_test DROP COLUMN col_no0;"
        )

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].alter_action, 'DROP COLUMN')
        self.assertEqual(statement.alter_specification[0].column_name, 'col_no0')

    def test_drop_primary_key(self):
        statement = alter_table_syntax.parseString(
            "ALTER TABLE test_test DROP PRIMARY KEY;"
        )

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].alter_action, 'DROP PRIMARY KEY')

    def test_drop_index(self):
        statement = alter_table_syntax.parseString(
            "ALTER TABLE test_test DROP INDEX idx_no0;"
        )

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].alter_action, 'DROP INDEX')
        self.assertEqual(statement.alter_specification[0].index_name, 'idx_no0')

    def test_drop_key(self):
        statement = alter_table_syntax.parseString(
            "ALTER TABLE test_test DROP KEY idx_no0;"
        )

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].alter_action, 'DROP INDEX')
        self.assertEqual(statement.alter_specification[0].index_name, 'idx_no0')

    def test_drop_foreign_key(self):
        statement = alter_table_syntax.parseString(
            "ALTER TABLE test_test DROP FOREIGN KEY fk_no0;"
        )

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].alter_action, 'DROP FOREIGN KEY')
        self.assertEqual(statement.alter_specification[0].fk_symbol, 'fk_no0')

    def test_drop_mixed(self):
        statement = alter_table_syntax.parseString("""
        ALTER TABLE test_test DROP col_no0,
            DROP COLUMN col_no1,
            DROP PRIMARY KEY,
            DROP INDEX idx_no0,
            DROP KEY idx_no1,
            DROP FOREIGN KEY fk_no0;
        """)

        self.assertFalse(statement.ignore)
        self.assertEqual(statement.statement_type, 'ALTER')
        self.assertEqual(statement.table_name, 'test_test')
        self.assertEqual(statement.alter_specification[0].alter_action, 'DROP COLUMN')
        self.assertEqual(statement.alter_specification[0].column_name, 'col_no0')
        self.assertEqual(statement.alter_specification[1].alter_action, 'DROP COLUMN')
        self.assertEqual(statement.alter_specification[1].column_name, 'col_no1')
        self.assertEqual(statement.alter_specification[2].alter_action, 'DROP PRIMARY KEY')
        self.assertEqual(statement.alter_specification[3].alter_action, 'DROP INDEX')
        self.assertEqual(statement.alter_specification[3].index_name, 'idx_no0')
        self.assertEqual(statement.alter_specification[4].alter_action, 'DROP INDEX')
        self.assertEqual(statement.alter_specification[4].index_name, 'idx_no1')
        self.assertEqual(statement.alter_specification[5].alter_action, 'DROP FOREIGN KEY')
        self.assertEqual(statement.alter_specification[5].fk_symbol, 'fk_no0')

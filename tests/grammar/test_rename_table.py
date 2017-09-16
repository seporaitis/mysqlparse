# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from mysqlparse.grammar.rename_table import rename_table_syntax


class RenameTableSyntaxTest(unittest.TestCase):

    def test_rename_table(self):
        statement = rename_table_syntax.parseString("""
        RENAME TABLE test1 TO test2;
        """)

        self.assertEqual(statement.statement_type, 'RENAME')
        self.assertFalse(statement.table_renamed[0].old_database_name)
        self.assertEqual(statement.table_renamed[0].old_table_name, 'test1')
        self.assertFalse(statement.table_renamed[0].new_database_name)
        self.assertEqual(statement.table_renamed[0].new_table_name, 'test2')

    def test_rename_multiple_tables(self):
        statement = rename_table_syntax.parseString("""
        RENAME TABLE
            test1 TO test2,
            test3 TO test4,
            test5 TO test6;
        """)

        self.assertEqual(statement.statement_type, 'RENAME')
        self.assertFalse(statement.table_renamed[0].old_database_name)
        self.assertEqual(statement.table_renamed[0].old_table_name, 'test1')
        self.assertFalse(statement.table_renamed[0].new_database_name)
        self.assertEqual(statement.table_renamed[0].new_table_name, 'test2')
        self.assertFalse(statement.table_renamed[1].old_database_name)
        self.assertEqual(statement.table_renamed[1].old_table_name, 'test3')
        self.assertFalse(statement.table_renamed[1].new_database_name)
        self.assertEqual(statement.table_renamed[1].new_table_name, 'test4')
        self.assertFalse(statement.table_renamed[2].old_database_name)
        self.assertEqual(statement.table_renamed[2].old_table_name, 'test5')
        self.assertFalse(statement.table_renamed[2].new_database_name)
        self.assertEqual(statement.table_renamed[2].new_table_name, 'test6')

    def test_rename_database_table(self):
        statement = rename_table_syntax.parseString("""
        RENAME TABLE db1.test1 TO db2.test2;
        """)

        self.assertEqual(statement.statement_type, 'RENAME')
        self.assertEqual(statement.table_renamed[0].old_database_name, 'db1')
        self.assertEqual(statement.table_renamed[0].old_table_name, 'test1')
        self.assertEqual(statement.table_renamed[0].new_database_name, 'db2')
        self.assertEqual(statement.table_renamed[0].new_table_name, 'test2')

    def test_rename_mixed_databases_tables(self):
        statement = rename_table_syntax.parseString("""
        RENAME TABLE
            db1.test1 TO db2.test2,
            test3 TO test4;
        """)

        self.assertEqual(statement.statement_type, 'RENAME')
        self.assertEqual(statement.table_renamed[0].old_database_name, 'db1')
        self.assertEqual(statement.table_renamed[0].old_table_name, 'test1')
        self.assertEqual(statement.table_renamed[0].new_database_name, 'db2')
        self.assertEqual(statement.table_renamed[0].new_table_name, 'test2')
        self.assertFalse(statement.table_renamed[1].old_database_name)
        self.assertEqual(statement.table_renamed[1].old_table_name, 'test3')
        self.assertFalse(statement.table_renamed[1].new_database_name)
        self.assertEqual(statement.table_renamed[1].new_table_name, 'test4')

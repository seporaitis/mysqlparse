# -*- encoding:utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
    )

import unittest

from mysqlparse.grammar.drop_table import drop_table_syntax


class DropTableSyntaxTest(unittest.TestCase):

    def test_drop_table(self):
        statement = drop_table_syntax.parseString("""
        DROP TABLE test;
        """)

        self.assertEqual(statement.statement_type, 'DROP')
        self.assertFalse(statement.temporary)
        self.assertFalse(statement.if_exists)
        self.assertFalse(statement.dropped[0].database_name)
        self.assertEqual(statement.dropped[0].table_name, 'test')

    def test_drop_multiple_tables(self):
        statement = drop_table_syntax.parseString("""
        DROP TABLE test, test_db.test_table, yet_another_test_table;
        """)

        self.assertEqual(statement.statement_type, 'DROP')
        self.assertFalse(statement.temporary)
        self.assertFalse(statement.if_exists)
        self.assertFalse(statement.dropped[0].database_name)
        self.assertEqual(statement.dropped[0].table_name, 'test')
        self.assertEqual(statement.dropped[1].database_name, 'test_db')
        self.assertEqual(statement.dropped[1].table_name, 'test_table')
        self.assertFalse(statement.dropped[2].database_name)
        self.assertEqual(statement.dropped[2].table_name,
                         'yet_another_test_table')

    def test_drop_temporary_table(self):
        statement = drop_table_syntax.parseString("""
        DROP TEMPORARY TABLE test;
        """)

        self.assertEqual(statement.statement_type, 'DROP')
        self.assertTrue(statement.temporary)
        self.assertFalse(statement.if_exists)
        self.assertFalse(statement.dropped[0].database_name)
        self.assertEqual(statement.dropped[0].table_name, 'test')

    def test_drop_table_if_exists(self):
        statement = drop_table_syntax.parseString("""
        DROP TABLE IF EXISTS test;
        """)

        self.assertEqual(statement.statement_type, 'DROP')
        self.assertFalse(statement.temporary)
        self.assertTrue(statement.if_exists)
        self.assertFalse(statement.dropped[0].database_name)
        self.assertEqual(statement.dropped[0].table_name, 'test')

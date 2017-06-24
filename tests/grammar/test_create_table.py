# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from mysqlparse.grammar.create_table import create_table_syntax


class CreateTableSyntaxTest(unittest.TestCase):

    def test_create_table(self):
        statement = create_table_syntax.parseString("""
        CREATE TABLE test_test
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertFalse(statement.temporary)
        self.assertTrue(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')

    def test_create_temporary_table(self):
        statement = create_table_syntax.parseString("""
        CREATE TEMPORARY TABLE test_test
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertTrue(statement.temporary)
        self.assertTrue(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')

    def test_create_table_overwrite(self):
        statement = create_table_syntax.parseString("""
        CREATE TABLE IF NOT EXISTS test_test
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertFalse(statement.temporary)
        self.assertFalse(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')

    def test_create_temporary_table_overwrite(self):
        statement = create_table_syntax.parseString("""
        CREATE TEMPORARY TABLE IF NOT EXISTS test_test
        """)

        self.assertEqual(statement.statement_type, 'CREATE')
        self.assertTrue(statement.temporary)
        self.assertFalse(statement.overwrite)
        self.assertEqual(statement.table_name, 'test_test')

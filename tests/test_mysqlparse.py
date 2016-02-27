# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from os import path
import unittest

import mysqlparse


class ParseTest(unittest.TestCase):

    def setUp(self):
        super(ParseTest, self).setUp()

        self.fixture_dir = path.join(path.dirname(__file__), "fixtures")

    def test_string(self):
        with open(path.join(self.fixture_dir, 'test.sql'), 'r') as f:
            sql_file = mysqlparse.parse(f.read())

        self.assertEqual(len(sql_file.statements), 2)
        self.assertEqual(sql_file.statements[0].table_name, 'test_table1')
        self.assertEqual(sql_file.statements[1].table_name, 'test_table2')

    def test_file(self):
        with open(path.join(self.fixture_dir, 'test.sql'), 'r') as f:
            sql_file = mysqlparse.parse(f)

        self.assertEqual(len(sql_file.statements), 2)
        self.assertEqual(sql_file.statements[0].table_name, 'test_table1')
        self.assertEqual(sql_file.statements[1].table_name, 'test_table2')

    def test_typeerror(self):
        with self.assertRaises(TypeError) as ctx:
            mysqlparse.parse(None)

        self.assertEqual(str(ctx.exception), "Expected file-like or string object, but got 'NoneType' instead.")

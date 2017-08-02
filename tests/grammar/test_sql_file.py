# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from mysqlparse.grammar.sql_file import sql_file_syntax


class SqlFileSyntaxTest(unittest.TestCase):

    def test_multiple_statements(self):
        sql_file = sql_file_syntax.parseString("""
        CREATE TABLE test_table1 (
           test_column1 INT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
           test_column2 INT(11) NOT NULL
        );

        ALTER TABLE test_table2 ADD col_no0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD col_no1 LONGTEXT NOT NULL,
            ADD col_no2 VARCHAR(200) NULL,
            ADD col_no3 BIT(8) AFTER col0;

        CREATE TABLE test_table3 (
           test_column INT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL
        );

        ALTER TABLE test_table4 ADD col_no0 BIT(8) NOT NULL DEFAULT 0 FIRST,
            ADD col_no1 LONGTEXT NOT NULL,
            ADD col_no2 VARCHAR(200) NULL,
            ADD col_no3 BIT(8) AFTER col0;

        """)

        self.assertEqual(len(sql_file.statements), 4)
        self.assertEqual(sql_file.statements[0].table_name, 'test_table1')
        self.assertEqual(sql_file.statements[1].table_name, 'test_table2')
        self.assertEqual(sql_file.statements[2].table_name, 'test_table3')
        self.assertEqual(sql_file.statements[3].table_name, 'test_table4')

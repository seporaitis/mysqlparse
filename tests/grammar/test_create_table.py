# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

import pyparsing

from mysqlparse.grammar.create_table import table_options_syntax


class TableOptionsSyntaxTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(table_options_syntax.parseString("").engine_name, '')
        self.assertEqual(table_options_syntax.parseString("").auto_increment_value, '')

    def test_engine(self):
        self.assertEqual(table_options_syntax.parseString("ENGINE 'InnoDB'").engine_name, 'InnoDB')
        self.assertEqual(table_options_syntax.parseString("ENGINE='InnoDB'").engine_name, 'InnoDB')
        self.assertEqual(table_options_syntax.parseString("ENGINE 'InnoDB'").auto_increment_value, '')
        self.assertEqual(table_options_syntax.parseString("ENGINE='InnoDB'").auto_increment_value, '')

    def test_auto_increment(self):
        self.assertEqual(table_options_syntax.parseString("AUTO_INCREMENT '10'").engine_name, '')
        self.assertEqual(table_options_syntax.parseString("AUTO_INCREMENT='10'").engine_name, '')
        self.assertEqual(table_options_syntax.parseString("AUTO_INCREMENT 10").engine_name, '')
        self.assertEqual(table_options_syntax.parseString("AUTO_INCREMENT=10").engine_name, '')

        self.assertEqual(table_options_syntax.parseString("AUTO_INCREMENT '10'").auto_increment_value, '10')
        self.assertEqual(table_options_syntax.parseString("AUTO_INCREMENT='10'").auto_increment_value, '10')
        self.assertEqual(table_options_syntax.parseString("AUTO_INCREMENT 10").auto_increment_value, '10')
        self.assertEqual(table_options_syntax.parseString("AUTO_INCREMENT=10").auto_increment_value, '10')

    def test_all(self):
        self.assertEqual(table_options_syntax.parseString("ENGINE 'InnoDB' AUTO_INCREMENT '10'").engine_name, 'InnoDB')
        self.assertEqual(table_options_syntax.parseString("ENGINE='InnoDB' AUTO_INCREMENT='10'").engine_name, 'InnoDB')
        self.assertEqual(table_options_syntax.parseString("ENGINE InnoDB AUTO_INCREMENT 10").engine_name, 'InnoDB')
        self.assertEqual(table_options_syntax.parseString("ENGINE=InnoDB AUTO_INCREMENT=10").engine_name, 'InnoDB')

        self.assertEqual(table_options_syntax.parseString("ENGINE 'InnoDB' AUTO_INCREMENT '10'").auto_increment_value, '10')
        self.assertEqual(table_options_syntax.parseString("ENGINE='InnoDB' AUTO_INCREMENT='10'").auto_increment_value, '10')
        self.assertEqual(table_options_syntax.parseString("ENGINE InnoDB AUTO_INCREMENT 10").auto_increment_value, '10')
        self.assertEqual(table_options_syntax.parseString("ENGINE=InnoDB AUTO_INCREMENT=10").auto_increment_value, '10')


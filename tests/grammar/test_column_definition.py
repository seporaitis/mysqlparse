# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from mysqlparse.grammar.column_definition import column_definition_syntax


class ColumnDefinitionSyntax(unittest.TestCase):

    def test_plain_field(self):
        self.assertEqual(column_definition_syntax.parseString("VARCHAR(255)").null, 'implicit')
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255)").default)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255)").auto_increment)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255)").index_type)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255)").comment)

    def test_nullable(self):
        self.assertEqual(column_definition_syntax.parseString("VARCHAR(255)").null, 'implicit')
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) NOT NULL").null)
        self.assertTrue(column_definition_syntax.parseString("VARCHAR(255) NULL").null)

        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) NOT NULL").default)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) NULL").default)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) NOT NULL").auto_increment)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) NULL").auto_increment)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) NOT NULL").index_type)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) NULL").index_type)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) NOT NULL").comment)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) NULL").comment)

    def test_default(self):
        self.assertEqual(column_definition_syntax.parseString("VARCHAR(255) DEFAULT 'test'").null, 'implicit')
        self.assertEqual(column_definition_syntax.parseString("VARCHAR(255) DEFAULT 'test'").default, 'test')
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) DEFAULT 'test'").auto_increment)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) DEFAULT 'test'").index_type)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) DEFAULT 'test'").comment)

    def test_auto_increment(self):
        self.assertEqual(column_definition_syntax.parseString("INT(11) AUTO_INCREMENT").null, 'implicit')
        self.assertFalse(column_definition_syntax.parseString("INT(11) AUTO_INCREMENT").default)
        self.assertTrue(column_definition_syntax.parseString("INT(11) AUTO_INCREMENT").auto_increment)
        self.assertFalse(column_definition_syntax.parseString("INT(11) AUTO_INCREMENT").index_type)
        self.assertFalse(column_definition_syntax.parseString("INT(11) AUTO_INCREMENT").comment)

    def test_unique_index(self):
        self.assertEqual(column_definition_syntax.parseString("INT(11) UNIQUE").null, 'implicit')
        self.assertFalse(column_definition_syntax.parseString("INT(11) UNIQUE").default)
        self.assertFalse(column_definition_syntax.parseString("INT(11) UNIQUE").auto_increment)
        self.assertEqual(column_definition_syntax.parseString("INT(11) UNIQUE").index_type, 'unique_key')
        self.assertFalse(column_definition_syntax.parseString("INT(11) UNIQUE").comment)

        self.assertEqual(column_definition_syntax.parseString("INT(11) UNIQUE KEY").null, 'implicit')
        self.assertFalse(column_definition_syntax.parseString("INT(11) UNIQUE KEY").default)
        self.assertFalse(column_definition_syntax.parseString("INT(11) UNIQUE KEY").auto_increment)
        self.assertEqual(column_definition_syntax.parseString("INT(11) UNIQUE KEY").index_type, 'unique_key')
        self.assertFalse(column_definition_syntax.parseString("INT(11) UNIQUE KEY").comment)

    def test_primary_key(self):
        self.assertEqual(column_definition_syntax.parseString("INT(11) KEY").null, 'implicit')
        self.assertFalse(column_definition_syntax.parseString("INT(11) KEY").default)
        self.assertFalse(column_definition_syntax.parseString("INT(11) KEY").auto_increment)
        self.assertEqual(column_definition_syntax.parseString("INT(11) KEY").index_type, 'primary_key')
        self.assertFalse(column_definition_syntax.parseString("INT(11) KEY").comment)

        self.assertEqual(column_definition_syntax.parseString("INT(11) PRIMARY KEY").null, 'implicit')
        self.assertFalse(column_definition_syntax.parseString("INT(11) PRIMARY KEY").default)
        self.assertFalse(column_definition_syntax.parseString("INT(11) PRIMARY KEY").auto_increment)
        self.assertEqual(column_definition_syntax.parseString("INT(11) PRIMARY KEY").index_type, 'primary_key')
        self.assertFalse(column_definition_syntax.parseString("INT(11) PRIMARY KEY").comment)

    def test_comment(self):
        self.assertEqual(column_definition_syntax.parseString("VARCHAR(255) COMMENT 'test'").null, 'implicit')
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) COMMENT 'test'").default)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) COMMENT 'test'").auto_increment)
        self.assertFalse(column_definition_syntax.parseString("VARCHAR(255) COMMENT 'test'").index_type)
        self.assertEqual(column_definition_syntax.parseString("VARCHAR(255) COMMENT 'test'").comment, 'test')

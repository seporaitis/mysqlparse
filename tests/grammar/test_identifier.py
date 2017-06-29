# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from pyparsing import ParseException

from mysqlparse.grammar.identifier import identifier_syntax


class IdentifierSyntaxTest(unittest.TestCase):

    def test_valid_unquoted(self):
        statement = identifier_syntax.parseString("valid_$name")
        self.assertEqual(statement[0], "valid_$name")

    def test_valid_backquoted(self):
        statement = identifier_syntax.parseString("`valid_$name`")
        self.assertEqual(statement[0], "valid_$name")

    def test_valid_singlequoted(self):
        statement = identifier_syntax.parseString("'valid_$name'")
        self.assertEqual(statement[0], "valid_$name")

    def test_valid_doublequoted(self):
        statement = identifier_syntax.parseString('"valid_$name"')
        self.assertEqual(statement[0], "valid_$name")

    def test_valid_backquoted_nonstandard(self):
        statement = identifier_syntax.parseString("`valid $name`")
        self.assertEqual(statement[0], "valid $name")

    def test_valid_singlequoted_nonstandard(self):
        statement = identifier_syntax.parseString("'valid $name'")
        self.assertEqual(statement[0], "valid $name")

    def test_valid_doublequoted_nonstandard(self):
        statement = identifier_syntax.parseString('"valid $name"')
        self.assertEqual(statement[0], "valid $name")

    def test_invalid_missing_backquote(self):
        with self.assertRaises(ParseException):
            identifier_syntax.parseString("`valid $name")

    def test_invalid_missing_singlequote(self):
        with self.assertRaises(ParseException):
            identifier_syntax.parseString("'valid $name")

    def test_invalid_missing_doublequote(self):
        with self.assertRaises(ParseException):
            identifier_syntax.parseString('"valid $name')

# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *

from mysqlparse.grammar.utils import stripQuotes


#
# SCHEMA OBJECT NAMES (IDENTIFIERS)
#
# Source: https://dev.mysql.com/doc/refman/5.7/en/identifiers.html
#

identifier_syntax = Or([
    Word(alphanums + "_$"),
    QuotedString('"'),
    QuotedString("`"),
    QuotedString("'")
]).setParseAction(stripQuotes)

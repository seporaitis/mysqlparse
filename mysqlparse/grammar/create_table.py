# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *

from mysqlparse.grammar.utils import stripQuotes


#
# CREATE TABLE SYNTAX
#
# Source: http://dev.mysql.com/doc/refman/5.7/en/create-table.html
#

table_options_syntax = Forward()
table_options_syntax <<= (
    Optional(CaselessKeyword("ENGINE") + Optional(Suppress("=")) + Word(alphas + "'").setName("engine_name").setParseAction(stripQuotes).setResultsName("engine_name")) +
    Optional(CaselessKeyword("AUTO_INCREMENT") + Optional(Suppress("=")) + Word(nums + "'").setName("auto_increment_value").setParseAction(stripQuotes).setResultsName("auto_increment_value"))
)
    

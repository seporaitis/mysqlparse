# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *

from mysqlparse.grammar.column_definition import column_definition_syntax
from mysqlparse.grammar.utils import stripQuotes, defaultValue


#
# PARTIAL PARSERS
#

_column_name = Word(alphanums + "`").setParseAction(stripQuotes)
_add = CaselessKeyword("ADD").setParseAction(replaceWith("ADD COLUMN")).setResultsName("alter_action")
_add_column = CaselessKeyword("ADD COLUMN").setResultsName("alter_action")
_column_position = Optional(
    Or([CaselessKeyword("FIRST"), Suppress(CaselessKeyword("AFTER")) + _column_name])
).setParseAction(defaultValue("LAST")).setResultsName("column_position")
_last_column = Empty().setParseAction(defaultValue("LAST")).setResultsName("column_position")

_alter_specification_syntax = Forward()
_alter_specification_syntax <<= (
    (Or([
        (_add + _column_name.setResultsName("column_name") + column_definition_syntax + _column_position),
        (_add_column + _column_name.setResultsName("column_name") + column_definition_syntax + _column_position),
        (_add_column +
         delimitedList(_column_name.setResultsName("column_name") + column_definition_syntax) +
         _last_column),
    ]))
)

_ignore = Optional(
    CaselessKeyword("IGNORE").setParseAction(replaceWith(True))
).setParseAction(defaultValue(False)).setResultsName("ignore")


#
# ALTER TABLE SYNTAX
#
# Source: http://dev.mysql.com/doc/refman/5.7/en/alter-table.html
#

alter_table_syntax = Forward()
alter_table_syntax <<= (
    CaselessKeyword("ALTER").setResultsName("statement_type") + _ignore + Suppress(Optional(CaselessKeyword("TABLE"))) +
    Word(alphanums + "`").setResultsName("table_name") +
    delimitedList(Group(_alter_specification_syntax).setResultsName("alter_specification", listAllMatches=True)) +
    Suppress(Optional(";"))
)

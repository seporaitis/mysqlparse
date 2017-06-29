# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *

from mysqlparse.grammar.column_definition import column_definition_syntax
from mysqlparse.grammar.utils import stripQuotes


#
# PARTIAL PARSERS
#

_column_name = Word(alphanums+ "`_").setParseAction(stripQuotes)

_column_specification_syntax = (_column_name.setResultsName("column_name") + column_definition_syntax)

_create_type = CaselessKeyword("TABLE").setResultsName("create_type")

_temporary = Optional(
    CaselessKeyword("TEMPORARY").setParseAction(replaceWith(True)),
    default=False,
).setResultsName("temporary")

_if_not_exists = Optional(
    CaselessKeyword("IF NOT EXISTS").setParseAction(replaceWith(False)),
    default=True,
).setResultsName("overwrite")

#
# CREATE TABLE SYNTAX
#
# Source: https://dev.mysql.com/doc/refman/5.7/en/create-table.htlmme
#

create_table_syntax = Forward()
create_table_syntax <<= (
    (CaselessKeyword("CREATE").setResultsName("statement_type") + _temporary +
     _create_type + _if_not_exists + Word(alphanums + "`_").setResultsName("table_name")) +
    (Suppress("(") + delimitedList(Group(_column_specification_syntax).setResultsName("column_specification", listAllMatches=True)) + Suppress(")"))
)

# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *

from mysqlparse.grammar.column_definition import column_definition_syntax
from mysqlparse.grammar.identifier import identifier_syntax


#
# PARTIAL PARSERS
#

_column_specification_syntax = (identifier_syntax.setResultsName("column_name") + column_definition_syntax)

_create_type = CaselessKeyword("TABLE").setResultsName("create_type")

_temporary = Optional(
    CaselessKeyword("TEMPORARY").setParseAction(replaceWith(True)),
    default=False,
).setResultsName("temporary")

_if_not_exists = Optional(
    CaselessKeyword("IF NOT EXISTS").setParseAction(replaceWith(False)),
    default=True,
).setResultsName("overwrite")

_table_option = Word(alphas + "_").setResultsName("key") + Optional(Suppress("=")) + identifier_syntax.setResultsName("value")

# TODO(JS): this is a *tweaked* duplicate from alter_table
_index_type = Optional(
    Suppress(CaselessKeyword("USING")) + Or([CaselessKeyword("BTREE"), CaselessKeyword("HASH")]),
    default=False
).setResultsName("index_type").setParseAction(lambda s, l, toks: toks[0])
_index_direction = Optional(Or([CaselessKeyword("ASC"), CaselessKeyword("DESC")]), default=None).setResultsName("direction")
_index_column = (
    identifier_syntax.setResultsName("column_name") +
    Optional(
        Suppress("(") +
        Word(nums) +
        Suppress(")"),
        default=False
    ).setResultsName("length").setParseAction(lambda s, l, toks: int(toks[0])) +
    _index_direction
)

_primary_key = (
    CaselessKeyword("CONSTRAINT") + identifier_syntax.setResultsName("symbol") +
    CaselessKeyword("PRIMARY KEY") + _index_type + Optional(
        Suppress("(") +
        delimitedList(
            OneOrMore(Group(_index_column).setResultsName("index_columns", listAllMatches=True))
        ) +
        Suppress(")")
    )
)

#
# CREATE TABLE SYNTAX
#
# Source: https://dev.mysql.com/doc/refman/5.7/en/create-table.html
#

create_table_syntax = (
    CaselessKeyword("CREATE").setResultsName("statement_type") + _temporary +
    _create_type + _if_not_exists + Word(alphanums + "`_").setResultsName("table_name") +
    Suppress("(") +
    delimitedList(
        OneOrMore(
            Or([
                Group(_column_specification_syntax).setResultsName("column_specification", listAllMatches=True),
                Group(_primary_key).setResultsName("constraints", listAllMatches=True)
            ])
        )
    ) +
    Suppress(")") +
    Optional(
        ZeroOrMore(Group(_table_option)), default=[]
    ).setResultsName("table_options") +
    Suppress(Optional(";"))
)

# -*- encoding:utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
    )

from pyparsing import (
    CaselessKeyword,
    Group,
    OneOrMore,
    Optional,
    delimitedList,
    replaceWith
    )

from mysqlparse.grammar.identifier import (
    database_name_syntax,
    identifier_syntax
    )

_drop_type = CaselessKeyword("TABLE").setResultsName("drop_type")

_temporary = Optional(
    CaselessKeyword("TEMPORARY").setParseAction(replaceWith(True)),
    default=False,
).setResultsName("temporary")

_if_not_exists = Optional(
    CaselessKeyword("IF EXISTS").setParseAction(replaceWith(True)),
    default=False,
).setResultsName("if_exists")

drop_table_syntax = (
    CaselessKeyword("DROP").setResultsName("statement_type") + _temporary +
    CaselessKeyword("TABLE") + _if_not_exists + delimitedList(
        OneOrMore(Group(database_name_syntax.setResultsName("database_name") +
                        identifier_syntax.setResultsName("table_name"))
                  .setResultsName("dropped", listAllMatches=True))
        )
    )

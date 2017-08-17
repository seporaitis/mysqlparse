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
    Suppress,
    delimitedList
    )

from mysqlparse.grammar.identifier import (
    identifier_syntax,
    database_name_syntax
    )

#
# PARTIAL PARSERS
#

_tables_renamed = (
    database_name_syntax.setResultsName("old_database_name") +
    identifier_syntax.setResultsName("old_table_name") +
    Suppress(CaselessKeyword("TO")) +
    database_name_syntax.setResultsName("new_database_name") +
    database_name_syntax + identifier_syntax.setResultsName("new_table_name")
    )

#
# RENAME TABLE SYNTAX
#
# Source: https://dev.mysql.com/doc/refman/5.7/en/rename-table.html
#

rename_table_syntax = (
    CaselessKeyword("RENAME").setResultsName("statement_type") +
    Suppress(Optional(CaselessKeyword("TABLE"))) +
    delimitedList(
        OneOrMore(Group(_tables_renamed)
                  .setResultsName("table_renamed", listAllMatches=True))
        ) +
    Suppress(Optional(";"))
)

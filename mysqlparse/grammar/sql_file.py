# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *

from mysqlparse.grammar.alter_table import alter_table_syntax
from mysqlparse.grammar.create_table import create_table_syntax
from mysqlparse.grammar.rename_table import rename_table_syntax
from mysqlparse.grammar.drop_table import drop_table_syntax


sql_file_syntax = (
    ZeroOrMore(
        Suppress(
            SkipTo(
                Or([
                    CaselessKeyword("ALTER"),
                    CaselessKeyword("CREATE"),
                    CaselessKeyword("RENAME"),
                    CaselessKeyword("DROP"),
                ])
            )
        ) +
        Group(
            Or([
                alter_table_syntax,
                create_table_syntax,
                rename_table_syntax,
                drop_table_syntax
            ])
        ).setResultsName("statements", listAllMatches=True)
    )
)

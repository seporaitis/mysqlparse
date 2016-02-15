# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *

from mysqlparse.grammar.alter_table import alter_table_syntax


sql_file_syntax = Forward()
sql_file_syntax <<= (
    ZeroOrMore(
        Suppress(SkipTo(CaselessKeyword("ALTER"))) +
        Group(alter_table_syntax).setResultsName("statements", listAllMatches=True)
    )
)

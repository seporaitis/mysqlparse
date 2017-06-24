# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *


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
# Source: https://dev.mysql.com/doc/refman/5.7/en/create-table.html
#

create_table_syntax = Forward()
create_table_syntax <<= (
    (CaselessKeyword("CREATE").setResultsName("statement_type") + _temporary +
     _create_type + _if_not_exists + Word(alphanums + "`_").setResultsName("table_name"))
)

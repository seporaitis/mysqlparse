# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from mysqlparse.grammar.sql_file import sql_file_syntax


def parse(file_or_string):
    """Parse a file-like object or string.

    Args:
        file_or_string (file, str): File-like object or string.

    Returns:
        ParseResults: instance of pyparsing parse results.
    """
    if hasattr(file_or_string, 'read') and hasattr(file_or_string.read, '__call__'):
        return sql_file_syntax.parseString(file_or_string.read())
    else:
        return sql_file_syntax.parseString(file_or_string)

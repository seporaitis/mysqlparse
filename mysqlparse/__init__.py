# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import six

from mysqlparse.grammar.sql_file import sql_file_syntax

__author__ = 'Julius Seporaitis'
__email__ = 'julius@seporaitis.net'
__version__ = '0.1.5'


def parse(file_or_string):
    """Parse a file-like object or string.

    Args:
        file_or_string (file, str): File-like object or string.

    Returns:
        ParseResults: instance of pyparsing parse results.
    """
    if hasattr(file_or_string, 'read') and hasattr(file_or_string.read, '__call__'):
        return sql_file_syntax.parseString(file_or_string.read())
    elif isinstance(file_or_string, six.string_types):
        return sql_file_syntax.parseString(file_or_string)
    else:
        raise TypeError("Expected file-like or string object, but got '{type_name}' instead.".format(
            type_name=type(file_or_string).__name__,
        ))

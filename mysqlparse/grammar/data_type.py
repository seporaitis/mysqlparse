# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *


#
# UTILITY FUNCTIONS
#

def define_basic_type(keyword, length_name=None):
    if not length_name:
        length_name = "length"
    return (
        CaselessKeyword(keyword) +
        Optional(Suppress("(") + Word(nums).setName("integer") + Suppress(")")).setResultsName(length_name)
    )


def define_decimal_type(keyword):
    return (
        CaselessKeyword(keyword) +
        Optional(
            Suppress("(") + Word(nums).setName("length").setResultsName("length") +
            Optional("," + Word(nums).setName("decimals").setResultsName("decimals")) +
            Suppress(")")
        ) +
        Optional(CaselessKeyword("UNSIGNED").setParseAction(replaceWith(True)).setResultsName("unsigned")) +
        Optional(CaselessKeyword("ZEROFILL").setParseAction(replaceWith(True)).setResultsName('zerofill'))
    )


def extend_to_integer_type(type_def):
    return (
        type_def +
        Optional(CaselessKeyword("UNSIGNED").setParseAction(replaceWith(True)).setResultsName("unsigned")) +
        Optional(CaselessKeyword("ZEROFILL").setParseAction(replaceWith(True)).setResultsName("zerofill"))
    )


def extend_to_character_type(type_def, binary=True):
    if binary:
        type_def += Optional(CaselessKeyword("BINARY").setParseAction(replaceWith(True)).setResultsName("binary"))
    return (
        type_def +
        Optional(CaselessKeyword("CHARACTER SET") + QuotedString("'").setResultsName("character_set")) +
        Optional(CaselessKeyword("COLLATE") + QuotedString("'").setResultsName("collation_name"))
    )


#
# DATA TYPE SYNTAX
#
# Source: http://dev.mysql.com/doc/refman/5.7/en/create-table.html
#

data_type_syntax = Forward()
data_type_syntax <<= (
    define_basic_type("BIT") |

    extend_to_integer_type(define_basic_type("TINYINT")) |
    extend_to_integer_type(define_basic_type("SMALLINT")) |
    extend_to_integer_type(define_basic_type("MEDIUMINT")) |
    extend_to_integer_type(define_basic_type("INT")) |
    extend_to_integer_type(define_basic_type("INTEGER")) |
    extend_to_integer_type(define_basic_type("BIGINT")) |

    define_decimal_type("REAL") |
    define_decimal_type("DOUBLE") |
    define_decimal_type("FLOAT") |
    define_decimal_type("DECIMAL") |
    define_decimal_type("NUMERIC") |

    CaselessKeyword("DATE") |

    define_basic_type("TIME", "precision") |
    define_basic_type("TIMESTAMP", "precision") |
    define_basic_type("DATETIME", "precision") |

    CaselessKeyword("YEAR") |

    extend_to_character_type(define_basic_type("CHAR")) |
    extend_to_character_type(
        CaselessKeyword("VARCHAR") +
        Suppress("(") + Word(nums).setName("integer").setResultsName("length") + Suppress(")")
    ) |

    define_basic_type("BINARY") |
    (
        CaselessKeyword("VARBINARY") +
        Suppress("(") + Word(nums).setName("integer").setResultsName("length") + Suppress(")")
    ) |

    CaselessKeyword("TINYBLOB") |
    CaselessKeyword("BLOB") |
    CaselessKeyword("MEDIUMBLOB") |
    CaselessKeyword("LONGBLOB") |

    extend_to_character_type(CaselessKeyword("TINYTEXT")) |
    extend_to_character_type(CaselessKeyword("TEXT")) |
    extend_to_character_type(CaselessKeyword("MEDIUMTEXT")) |
    extend_to_character_type(CaselessKeyword("LONGTEXT")) |

    extend_to_character_type(
        (
            CaselessKeyword("ENUM") +
            Suppress("(") +
            delimitedList(QuotedString("'")).setName("enum_values").setResultsName("value_list") +
            Suppress(")")
        ),
        binary=False
    ) |
    extend_to_character_type(
        (
            CaselessKeyword("SET") +
            Suppress("(") +
            delimitedList(QuotedString("'")).setName("set_values").setResultsName("value_list") +
            Suppress(")")
        ),
        binary=False
    )
).setResultsName("data_type")

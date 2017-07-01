# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from pyparsing import *

from mysqlparse.grammar.column_definition import column_definition_syntax
from mysqlparse.grammar.identifier import identifier_syntax


#
# PARTIAL PARSERS
#

_database_name = (Optional(identifier_syntax + FollowedBy('.') +
                           Suppress('.'), default=None)
                  .setResultsName("database_name")
                  .setParseAction(lambda s, l, toks: toks[0]))

# ADD COLUMN
_column_name = identifier_syntax.setResultsName("column_name")
_add = CaselessKeyword("ADD").setParseAction(replaceWith("ADD COLUMN")).setResultsName("alter_action")
_add_column = CaselessKeyword("ADD COLUMN").setResultsName("alter_action")
_column_position = Optional(
    Or([CaselessKeyword("FIRST"), Suppress(CaselessKeyword("AFTER")) + identifier_syntax]),
    default="LAST"
).setResultsName("column_position")
_last_column = Empty().setParseAction(lambda s, l, toks: ["LAST"]).setResultsName("column_position")

_alter_column_specification = [
    (_add + _column_name + column_definition_syntax + _column_position),
    (_add_column + _column_name + column_definition_syntax + _column_position),
    (_add_column + delimitedList(_column_name + column_definition_syntax) + _last_column),
]

# ADD INDEX
_index_name = identifier_syntax.setResultsName("index_name")
_add_index = Or([
    CaselessKeyword("ADD INDEX").setResultsName("alter_action"),
    CaselessKeyword("ADD KEY").setParseAction(replaceWith("ADD INDEX")).setResultsName("alter_action"),
])
_index_type = Optional(
    Suppress(CaselessKeyword("USING")) + Or([CaselessKeyword("BTREE"), CaselessKeyword("HASH")]),
    default=None
).setResultsName("index_type")
_index_direction = Optional(Or([CaselessKeyword("ASC"), CaselessKeyword("DESC")]), default=None).setResultsName("direction")
_index_column = (
    _column_name +
    Optional(Suppress("(") + Word(nums) + Suppress(")"), default=None).setResultsName("length") +
    _index_direction
)

_index_option = (
    Optional(
        Suppress(CaselessKeyword("KEY_BLOCK_SIZE")) + Suppress(Optional("=")) + Word(nums),
        default=None
    ).setResultsName("key_block_size") +
    _index_type +
    Optional(
        Suppress(CaselessKeyword("WITH PARSER")) + identifier_syntax,
        default=None,
    ).setResultsName("parser_name") +
    Optional(
        Suppress(CaselessKeyword("COMMENT")) + Or([QuotedString("'"), QuotedString('"')]),
        default=None,
    ).setResultsName("comment")
)


_alter_index_specification = [
    (_add_index + _index_name + _index_type +
     Suppress("(") +
     delimitedList(OneOrMore(Group(_index_column).setResultsName("index_columns", listAllMatches=True))) +
     Suppress(")") +
     _index_option),
]

# MODIFY COLUMN
_modify = CaselessKeyword("MODIFY").setParseAction(replaceWith("MODIFY COLUMN")).setResultsName("alter_action")
_modify_column = CaselessKeyword("MODIFY COLUMN").setResultsName("alter_action")


_modify_column_specification = [
    (_modify + _column_name + column_definition_syntax + _column_position),
    (_modify_column + _column_name + column_definition_syntax + _column_position),
    (_modify_column + delimitedList(_column_name + column_definition_syntax) + _last_column),
]

# CHANGE COLUMN
_change = CaselessKeyword("CHANGE").setParseAction(replaceWith("CHANGE COLUMN")).setResultsName("alter_action")
_change_column = CaselessKeyword("CHANGE COLUMN").setResultsName("alter_action")


_change_column_specification = [
    (_change + _column_name +
     identifier_syntax.setResultsName("new_column_name") +
     column_definition_syntax + _column_position),
    (_change_column + _column_name +
     identifier_syntax.setResultsName("new_column_name") +
     column_definition_syntax + _column_position),
    (_change_column +
     delimitedList(_column_name +
                   identifier_syntax.setResultsName("new_column_name") +
                   column_definition_syntax) + _last_column),
]


# DROP
_fk_symbol = identifier_syntax.setResultsName("fk_symbol")

_drop = CaselessKeyword("DROP").setParseAction(replaceWith("DROP COLUMN")).setResultsName("alter_action")
_drop_column = CaselessKeyword("DROP COLUMN").setResultsName("alter_action")
_drop_pk = CaselessKeyword("DROP PRIMARY KEY").setResultsName("alter_action")
_drop_index = CaselessKeyword("DROP INDEX").setResultsName("alter_action")
_drop_key = CaselessKeyword("DROP KEY").setParseAction(replaceWith("DROP INDEX")).setResultsName("alter_action")
_drop_fk = CaselessKeyword("DROP FOREIGN KEY").setResultsName("alter_action")


_drop_specification = [
    (_drop + _column_name),
    (_drop_column + _column_name),
    (_drop_pk),
    (_drop_index + _index_name),
    (_drop_key + _index_name),
    (_drop_fk + _fk_symbol),
]


_alter_specification_syntax = Forward()
_alter_specification_syntax <<= (
    (Or(
        _alter_column_specification +
        _alter_index_specification +
        _modify_column_specification +
        _change_column_specification +
        _drop_specification
    ))
)

_ignore = Optional(
    CaselessKeyword("IGNORE").setParseAction(replaceWith(True)),
    default=False,
).setResultsName("ignore")


#
# ALTER TABLE SYNTAX
#
# Source: http://dev.mysql.com/doc/refman/5.7/en/alter-table.html
#

alter_table_syntax = Forward()
alter_table_syntax <<= (
    CaselessKeyword("ALTER").setResultsName("statement_type") + _ignore + Suppress(Optional(CaselessKeyword("TABLE"))) +
    _database_name + identifier_syntax.setResultsName("table_name") +
    delimitedList(Group(_alter_specification_syntax).setResultsName("alter_specification", listAllMatches=True)) +
    Suppress(Optional(";"))
)

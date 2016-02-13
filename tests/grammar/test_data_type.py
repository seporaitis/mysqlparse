# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

import pyparsing

from mysqlparse.grammar.data_type import data_type_syntax


class DataTypeSyntaxTest(unittest.TestCase):

    def test_bit(self):
        self.assertEquals(data_type_syntax.parseString("BIT").data_type, 'BIT')
        self.assertEquals(data_type_syntax.parseString("BIT(8)").data_type, 'BIT')
        self.assertEquals(data_type_syntax.parseString("BIT(8)").length[0], '8')

    def test_integers(self):
        type_list = ['TINYINT', 'SMALLINT', 'MEDIUMINT', 'INT', 'INTEGER', 'BIGINT']

        type_plain = "{type_name}".format
        type_with_length = "{type_name}(8)".format
        type_with_unsigned = "{type_name}(8) unsigned".format
        type_with_zerofill = "{type_name}(8) zerofill".format
        type_with_all_modifiers = "{type_name}(8) UNSIGNED ZEROFILL".format

        for type_name in type_list:
            self.assertEquals(
                data_type_syntax.parseString(type_plain(type_name=type_name)).data_type,
                type_name,
            )

            self.assertEquals(
                data_type_syntax.parseString(type_with_length(type_name=type_name)).data_type,
                type_name,
            )
            self.assertEquals(
                data_type_syntax.parseString(type_with_length(type_name=type_name)).length[0],
                '8',
            )
            self.assertFalse(
                data_type_syntax.parseString(type_with_length(type_name=type_name)).unsigned,
            )
            self.assertFalse(
                data_type_syntax.parseString(type_with_length(type_name=type_name)).zerofill,
            )

            self.assertEquals(
                data_type_syntax.parseString(type_with_unsigned(type_name=type_name)).data_type,
                type_name,
            )
            self.assertEquals(
                data_type_syntax.parseString(type_with_unsigned(type_name=type_name)).length[0],
                '8',
            )
            self.assertTrue(
                data_type_syntax.parseString(type_with_unsigned(type_name=type_name)).unsigned,
            )

            self.assertEquals(
                data_type_syntax.parseString(type_with_zerofill(type_name=type_name)).data_type,
                type_name,
            )
            self.assertEquals(
                data_type_syntax.parseString(type_with_zerofill(type_name=type_name)).length[0],
                '8',
            )
            self.assertTrue(
                data_type_syntax.parseString(type_with_zerofill(type_name=type_name)).zerofill,
            )

            self.assertEquals(
                data_type_syntax.parseString(type_with_all_modifiers(type_name=type_name)).data_type,
                type_name,
            )
            self.assertEquals(
                data_type_syntax.parseString(type_with_all_modifiers(type_name=type_name)).length[0],
                '8',
            )
            self.assertTrue(
                data_type_syntax.parseString(type_with_all_modifiers(type_name=type_name)).unsigned,
            )
            self.assertTrue(
                data_type_syntax.parseString(type_with_all_modifiers(type_name=type_name)).zerofill,
            )

    def test_decimals(self):
        type_list = ['REAL', 'DOUBLE', 'FLOAT', 'DECIMAL', 'NUMERIC']

        for type_name in type_list:
            self.assertEquals(
                data_type_syntax.parseString("{type_name}".format(type_name=type_name)).data_type,
                type_name,
            )

            self.assertEquals(
                data_type_syntax.parseString("{type_name}(10)".format(type_name=type_name)).data_type,
                type_name,
            )
            self.assertEquals(
                data_type_syntax.parseString("{type_name}(10)".format(type_name=type_name)).length,
                '10',
            )
            self.assertEquals(
                data_type_syntax.parseString("{type_name}(10, 2)".format(type_name=type_name)).decimals,
                '2',
            )
            self.assertFalse(
                data_type_syntax.parseString("{type_name}(10, 2)".format(type_name=type_name)).unsigned,
            )
            self.assertFalse(
                data_type_syntax.parseString("{type_name}(10, 2)".format(type_name=type_name)).zerofill,
            )

            self.assertTrue(
                data_type_syntax.parseString("{type_name}(10, 2) UNSIGNED".format(type_name=type_name)).unsigned,
            )
            self.assertTrue(
                data_type_syntax.parseString("{type_name}(10, 2) ZEROFILL".format(type_name=type_name)).zerofill,
            )

            self.assertTrue(
                data_type_syntax.parseString("{type_name}(10, 2) UNSIGNED ZEROFILL".format(type_name=type_name)).unsigned,
            )
            self.assertTrue(
                data_type_syntax.parseString("{type_name}(10, 2) UNSIGNED ZEROFILL".format(type_name=type_name)).zerofill,
            )

    def test_datetimes(self):
        self.assertEquals(data_type_syntax.parseString("DATE").data_type, 'DATE')
        self.assertEquals(data_type_syntax.parseString("YEAR").data_type, 'YEAR')

        type_list = ['TIME', 'TIMESTAMP', 'DATETIME']

        type_plain = "{type_name}".format
        type_with_precision = "{type_name}(6)".format

        for type_name in type_list:
            self.assertEquals(
                data_type_syntax.parseString(type_plain(type_name=type_name)).data_type,
                type_name,
            )

            self.assertEquals(
                data_type_syntax.parseString(type_with_precision(type_name=type_name)).data_type,
                type_name,
            )
            self.assertEquals(
                data_type_syntax.parseString(type_with_precision(type_name=type_name)).precision[0],
                '6',
            )

    def test_chars(self):
        self.assertEquals(data_type_syntax.parseString("CHAR").data_type, 'CHAR')
        self.assertEquals(data_type_syntax.parseString("CHAR(8)").length[0], '8')
        self.assertEquals(data_type_syntax.parseString("CHAR(8) BINARY").length[0], '8')
        self.assertEquals(data_type_syntax.parseString("CHAR(8) BINARY").binary, True)
        self.assertEquals(data_type_syntax.parseString("CHAR(8) CHARACTER SET 'utf8'").character_set, "utf8")
        self.assertEquals(data_type_syntax.parseString("CHAR(8) COLLATE 'utf8_general'").collation_name, "utf8_general")
        self.assertEquals(
            data_type_syntax.parseString(
                "CHAR(8) BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general'"
            ).character_set,
            "utf8"
        )
        self.assertEquals(
            data_type_syntax.parseString(
                "CHAR(8) BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general'"
            ).collation_name,
            "utf8_general"
        )
        self.assertTrue(
            data_type_syntax.parseString(
                "CHAR(8) BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general'"
            ).binary,
        )

    def test_varchar(self):
        with self.assertRaises(pyparsing.ParseException):
            data_type_syntax.parseString("VARCHAR").data_type

        self.assertEquals(data_type_syntax.parseString("VARCHAR(8)").length[0], '8')
        self.assertEquals(data_type_syntax.parseString("VARCHAR(8) BINARY").length[0], '8')
        self.assertEquals(data_type_syntax.parseString("VARCHAR(8) BINARY").binary, True)
        self.assertEquals(data_type_syntax.parseString("VARCHAR(8) CHARACTER SET 'utf8'").character_set, "utf8")
        self.assertEquals(
            data_type_syntax.parseString("VARCHAR(8) COLLATE 'utf8_general'").collation_name,
            "utf8_general",
        )
        self.assertEquals(
            data_type_syntax.parseString(
                "VARCHAR(8) BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general'"
            ).character_set,
            "utf8"
        )
        self.assertEquals(
            data_type_syntax.parseString(
                "VARCHAR(8) BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general'"
            ).collation_name,
            "utf8_general"
        )
        self.assertTrue(
            data_type_syntax.parseString(
                "VARCHAR(8) BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general'"
            ).binary,
        )

    def test_binary(self):
        self.assertEquals(data_type_syntax.parseString("BINARY").data_type, 'BINARY')
        self.assertEquals(data_type_syntax.parseString("BINARY(8)").data_type, 'BINARY')
        self.assertEquals(data_type_syntax.parseString("BINARY(8)").length[0], '8')

    def test_varbinary(self):
        with self.assertRaises(pyparsing.ParseException):
            data_type_syntax.parseString("VARBINARY").data_type

        self.assertEquals(data_type_syntax.parseString("VARBINARY(8)").length[0], '8')

    def test_blobs(self):
        type_list = ['TINYBLOB', 'BLOB', 'MEDIUMBLOB', 'LONGBLOB']

        for type_name in type_list:
            self.assertEquals(data_type_syntax.parseString(type_name).data_type, type_name)

    def test_texts(self):
        type_list = ['TINYTEXT', 'TEXT', 'MEDIUMTEXT', 'LONGTEXT']

        for type_name in type_list:
            self.assertEquals(data_type_syntax.parseString(type_name).data_type, type_name)

            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name} BINARY".format(type_name=type_name)
                ).data_type,
                type_name,
            )
            self.assertTrue(
                data_type_syntax.parseString(
                    "{type_name} BINARY".format(type_name=type_name)
                ).binary,
            )

            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name} CHARACTER SET 'utf8'".format(type_name=type_name)
                ).data_type,
                type_name,
            )
            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name} CHARACTER SET 'utf8'".format(type_name=type_name)
                ).character_set,
                'utf8',
            )

            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name} COLLATE 'utf8_general_ci'".format(type_name=type_name)
                ).data_type,
                type_name,
            )
            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name} COLLATE 'utf8_general_ci'".format(type_name=type_name)
                ).collation_name,
                'utf8_general_ci',
            )
            self.assertFalse(
                data_type_syntax.parseString(
                    "{type_name} COLLATE 'utf8_general_ci'".format(type_name=type_name)
                ).binary,
            )

            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name} BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general_ci'".format(type_name=type_name)
                ).data_type,
                type_name,
            )
            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name} BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general_ci'".format(type_name=type_name)
                ).character_set,
                'utf8',
            )
            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name} BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general_ci'".format(type_name=type_name)
                ).collation_name,
                'utf8_general_ci',
            )
            self.assertTrue(
                data_type_syntax.parseString(
                    "{type_name} BINARY CHARACTER SET 'utf8' COLLATE 'utf8_general_ci'".format(type_name=type_name)
                ).binary,
            )

    def test_enumerables(self):
        type_list = ['ENUM', 'SET']

        for type_name in type_list:
            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name}('option1', 'option2', 'option3')".format(type_name=type_name)
                ).data_type,
                type_name,
            )

            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name}('option1', 'option2', 'option3')".format(type_name=type_name)
                ).value_list.asList(),
                ['option1', 'option2', 'option3'],
            )

            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name}('option1', 'option2', 'option3') CHARACTER SET 'utf8'".format(type_name=type_name)
                ).value_list.asList(),
                ['option1', 'option2', 'option3'],
            )
            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name}('option1', 'option2', 'option3') CHARACTER SET 'utf8'".format(type_name=type_name)
                ).character_set,
                'utf8',
            )

            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name}('option1', 'option2', 'option3') CHARACTER SET 'utf8'".format(type_name=type_name)
                ).value_list.asList(),
                ['option1', 'option2', 'option3'],
            )
            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name}('option1', 'option2', 'option3') CHARACTER SET 'utf8'".format(type_name=type_name)
                ).character_set,
                'utf8',
            )
            self.assertEquals(
                data_type_syntax.parseString(
                    "{type_name}('option1', 'option2', 'option3') CHARACTER SET 'utf8' COLLATE 'utf8_general_ci'".format(
                        type_name=type_name
                    )
                ).collation_name,
                'utf8_general_ci',
            )

import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import parser

class Tests(unittest.TestCase):

    def test_1(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_2(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/bool.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/bool.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_3(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_4(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/hetergeneous.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/hetergeneous.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_5(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/mixed-int-array.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/mixed-int-array.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_6(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/mixed-int-float.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/mixed-int-float.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_7(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/mixed-int-string.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/mixed-int-string.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_8(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/mixed-string-table.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/mixed-string-table.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_9(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nested-double.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nested-double.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_10(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nested-inline-table.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nested-inline-table.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_11(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nested.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nested.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_12(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nospaces.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nospaces.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_13(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-quote-comma-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-quote-comma-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_14(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-quote-comma.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-quote-comma.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_15(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-with-comma-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-with-comma-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_16(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-with-comma.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-with-comma.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_17(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/strings.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/strings.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_18(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-array-string-backslash.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-array-string-backslash.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_19(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/bool.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/bool.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_20(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/at-eof.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/at-eof.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_21(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/at-eof2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/at-eof2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_22(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/everywhere.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/everywhere.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_23(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/noeol.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/noeol.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_24(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nonascii.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nonascii.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_25(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/tricky.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/tricky.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_26(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/datetime.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/datetime.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_27(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-date.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-date.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_28(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-time.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-time.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_29(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_30(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/milliseconds.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/milliseconds.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_31(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/timezone.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/timezone.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_32(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty-file.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty-file.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_33(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/example.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/example.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_34(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/exponent.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/exponent.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_35(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_36(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inf-and-nan.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inf-and-nan.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_37(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/long.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/long.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_38(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/underscore.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/underscore.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_39(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/zero.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/zero.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_40(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/implicit-and-explicit-after.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/implicit-and-explicit-after.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_41(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/implicit-and-explicit-before.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/implicit-and-explicit-before.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_42(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/implicit-groups.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/implicit-groups.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_43(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_44(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/bool.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/bool.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_45(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_46(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/end-in-bool.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/end-in-bool.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_47(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_48(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/key-dotted.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/key-dotted.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_49(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/multiline.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/multiline.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_50(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nest.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nest.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_51(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/integer.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/integer.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_52(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/literals.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/literals.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_53(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/long.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/long.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_54(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/underscore.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/underscore.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_55(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/zero.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/zero.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_56(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/alphanum.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/alphanum.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_57(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/case-sensitive.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/case-sensitive.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_58(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/dotted-empty.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/dotted-empty.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_59(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/dotted.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/dotted.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_60(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_61(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/equals-nospace.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/equals-nospace.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_62(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/escapes.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/escapes.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_63(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/numeric-dotted.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/numeric-dotted.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_64(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/numeric.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/numeric.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_65(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/quoted-dots.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/quoted-dots.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_66(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/quoted-unicode.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/quoted-unicode.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_67(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/space.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/space.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_68(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/special-chars.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/special-chars.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_69(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/special-word.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/special-word.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_70(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/newline-crlf.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/newline-crlf.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_71(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/newline-lf.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/newline-lf.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_72(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec-example-1-compact.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec-example-1-compact.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_73(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec-example-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec-example-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_74(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_75(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_76(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-of-tables-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-of-tables-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_77(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-of-tables-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-of-tables-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_78(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-of-tables-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-of-tables-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_79(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/boolean-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/boolean-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_80(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_81(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_82(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_83(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_84(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_85(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_86(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_87(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table-3.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table-3.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_88(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/integer-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/integer-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_89(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/integer-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/integer-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_90(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/integer-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/integer-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_91(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/key-value-pair-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/key-value-pair-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_92(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_93(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_94(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-3.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-3.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_95(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-4.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-4.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_96(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-5.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-5.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_97(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-6.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-6.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_98(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-7.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keys-7.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_99(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-date-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-date-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_100(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-date-time-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-date-time-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_101(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-time-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/local-time-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_102(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/offset-date-time-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/offset-date-time-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_103(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/offset-date-time-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/offset-date-time-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_104(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_105(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_106(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_107(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-3.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-3.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_108(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-4.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-4.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_109(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-5.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-5.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_110(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-6.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-6.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_111(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-7.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string-7.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_112(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_113(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_114(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_115(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-3.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-3.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_116(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-4.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-4.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_117(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-5.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-5.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_118(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-6.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-6.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_119(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-7.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-7.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_120(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-8.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-8.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_121(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-9.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table-9.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_122(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/double-quote-escape.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/double-quote-escape.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_123(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_124(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/escape-tricky.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/escape-tricky.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_125(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/escaped-escape.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/escaped-escape.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_126(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/escapes.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/escapes.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_127(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/multiline-escaped-crlf.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/multiline-escaped-crlf.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_128(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/multiline-quotes.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/multiline-quotes.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_129(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/multiline.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/multiline.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_130(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nl.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/nl.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_131(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/quoted-unicode.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/quoted-unicode.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_132(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/raw-multiline.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/raw-multiline.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_133(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/raw.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/raw.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_134(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/simple.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/simple.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_135(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/unicode-escape.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/unicode-escape.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_136(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/unicode-literal.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/unicode-literal.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_137(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/with-pound.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/with-pound.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_138(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-implicit-and-explicit-after.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-implicit-and-explicit-after.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_139(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-implicit.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-implicit.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_140(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-many.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-many.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_141(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-nest.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-nest.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_142(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-one.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-one.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_143(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-table-array.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-table-array.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_144(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-within-dotted.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/array-within-dotted.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_145(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty-name.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty-name.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_146(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/empty.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_147(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keyword.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/keyword.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_148(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/names.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/names.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_149(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/no-eol.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/no-eol.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_150(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/sub-empty.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/sub-empty.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_151(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/sub.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/sub.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_152(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/whitespace.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/whitespace.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_153(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/with-literal-string.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/with-literal-string.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_154(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/with-pound.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/with-pound.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_155(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/with-single-quotes.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/with-single-quotes.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

    def test_156(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/without-super.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/without-super.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)

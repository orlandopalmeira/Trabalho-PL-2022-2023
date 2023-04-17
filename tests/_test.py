import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import parser

def parseBool(string):
    if string == 'true':
        return True
    elif string == 'false':
        return False
    else:
        raise ValueError()

def parseInt(string):
    return int(string)

def parseFloat(string):
    return float(string)

def parseVal(string):
    try:
        return parseInt(string)
    except:
        try:
            return parseFloat(string)
        except:
            try:
                return parseBool(string)
            except:
                return string

def parseAll(elem):
    if isinstance(elem,dict):
        return {k:parseAll(v) for k,v in elem.items()}
    elif isinstance(elem,list):
        return [parseAll(x) for x in elem]
    else:
        return parseVal(elem)

#! Converte os dicionários dos json de teste para um formato válido para nós
def convert_dict(dic):
    aux = lambda x: parseVal(x['value']) if (isinstance(x,dict) and 'type' in x and 'value' in x and len(x) == 2) else x
    dic = aux(dic)
    if isinstance(dic, dict):
        for k,v in dic.items():
            if isinstance(v,list):
                dic[k] = [convert_dict(x) for x in v]
            elif isinstance(v,dict):
                dic[k] = convert_dict(aux(v))
            else:
                dic[k] = parseVal(v)
    elif isinstance(dic,list):
        return [convert_dict(x) for x in dic]
    return dic

class Tests(unittest.TestCase):

    def test_1(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/array.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/array.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_2(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/bool.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/bool.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_3(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/empty.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/empty.json'))) as f_result:
                correct = json.load(f_result)
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_4(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/hetergeneous.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/hetergeneous.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_5(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/mixed-int-array.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/mixed-int-array.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_6(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/mixed-int-float.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/mixed-int-float.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_7(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/mixed-int-string.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/mixed-int-string.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_8(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/mixed-string-table.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/mixed-string-table.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_9(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/nested-double.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/nested-double.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_10(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/nested-inline-table.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/nested-inline-table.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_11(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/nested.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/nested.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_12(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/nospaces.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/nospaces.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_13(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/string-quote-comma-2.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/string-quote-comma-2.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_14(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/string-quote-comma.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/string-quote-comma.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_15(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/string-with-comma-2.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/string-with-comma-2.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_16(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/string-with-comma.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/string-with-comma.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_17(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/strings.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/strings.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_18(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/table-array-string-backslash.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/array/table-array-string-backslash.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_19(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/bool/bool.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/bool/bool.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_20(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/at-eof.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/at-eof.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_21(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/at-eof2.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/at-eof2.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_22(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/everywhere.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/everywhere.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_23(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/noeol.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/noeol.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_24(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/nonascii.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/nonascii.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_25(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/tricky.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/comment/tricky.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_26(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/datetime.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/datetime.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_27(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/local-date.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/local-date.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_28(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/local-time.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/local-time.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_29(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/local.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/local.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_30(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/milliseconds.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/milliseconds.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_31(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/no-seconds.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/no-seconds.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_32(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/timezone.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/datetime/timezone.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_33(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/empty-file.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/empty-file.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_34(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/example.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/example.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_35(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/exponent.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/exponent.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_36(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/float.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/float.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_37(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/inf-and-nan.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/inf-and-nan.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_38(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/long.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/long.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_39(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/underscore.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/underscore.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_40(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/zero.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/float/zero.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_41(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/implicit-and-explicit-after.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/implicit-and-explicit-after.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_42(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/implicit-and-explicit-before.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/implicit-and-explicit-before.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_43(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/implicit-groups.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/implicit-groups.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_44(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/array.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/array.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_45(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/bool.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/bool.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_46(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/empty.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/empty.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_47(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/end-in-bool.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/end-in-bool.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_48(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/inline-table.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/inline-table.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_49(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/key-dotted.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/key-dotted.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_50(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/multiline.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/multiline.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_51(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/nest.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/nest.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_52(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/newline.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/inline-table/newline.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_53(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/integer.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/integer.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_54(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/literals.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/literals.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_55(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/long.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/long.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_56(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/underscore.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/underscore.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_57(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/zero.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/integer/zero.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_58(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/alphanum.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/alphanum.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_59(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/case-sensitive.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/case-sensitive.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_60(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/dotted-empty.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/dotted-empty.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_61(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/dotted.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/dotted.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_62(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/empty.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/empty.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_63(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/equals-nospace.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/equals-nospace.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_64(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/escapes.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/escapes.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_65(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/numeric-dotted.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/numeric-dotted.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_66(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/numeric.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/numeric.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_67(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/quoted-dots.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/quoted-dots.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_68(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/quoted-unicode.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/quoted-unicode.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_69(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/space.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/space.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_70(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/special-chars.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/special-chars.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_71(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/special-word.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/special-word.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_72(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/unicode.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/key/unicode.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_73(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/newline-crlf.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/newline-crlf.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_74(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/newline-lf.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/newline-lf.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_75(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec-example-1-compact.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec-example-1-compact.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_76(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec-example-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec-example-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_77(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_78(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_79(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-of-tables-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-of-tables-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_80(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-of-tables-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-of-tables-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_81(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-of-tables-2.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/array-of-tables-2.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_82(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/boolean-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/boolean-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_83(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/comment-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/comment-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_84(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/float-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/float-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_85(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/float-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/float-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_86(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/float-2.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/float-2.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_87(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/inline-table-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/inline-table-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_88(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/inline-table-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/inline-table-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_89(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/inline-table-2.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/inline-table-2.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_90(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/inline-table-3.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/inline-table-3.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_91(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/integer-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/integer-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_92(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/integer-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/integer-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_93(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/integer-2.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/integer-2.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_94(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/key-value-pair-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/key-value-pair-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_95(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_96(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_97(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-3.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-3.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_98(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-4.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-4.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_99(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-5.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-5.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_100(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-6.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-6.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_101(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-7.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/keys-7.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_102(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/local-date-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/local-date-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_103(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/local-date-time-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/local-date-time-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_104(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/local-time-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/local-time-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_105(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/offset-date-time-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/offset-date-time-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_106(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/offset-date-time-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/offset-date-time-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_107(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_108(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_109(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-2.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-2.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_110(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-3.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-3.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_111(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-4.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-4.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_112(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-5.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-5.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_113(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-6.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-6.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_114(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-7.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/string-7.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_115(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-0.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-0.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_116(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-1.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-1.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_117(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-2.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-2.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_118(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-3.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-3.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_119(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-4.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-4.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_120(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-5.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-5.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_121(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-6.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-6.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_122(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-7.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-7.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_123(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-8.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-8.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_124(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-9.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/spec/table-9.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_125(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/double-quote-escape.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/double-quote-escape.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_126(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/empty.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/empty.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_127(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/escape-esc.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/escape-esc.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_128(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/escape-tricky.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/escape-tricky.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_129(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/escaped-escape.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/escaped-escape.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_130(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/escapes.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/escapes.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_131(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/hex-escape.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/hex-escape.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_132(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/multiline-escaped-crlf.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/multiline-escaped-crlf.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_133(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/multiline-quotes.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/multiline-quotes.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_134(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/multiline.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/multiline.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_135(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/nl.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/nl.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_136(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/quoted-unicode.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/quoted-unicode.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_137(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/raw-multiline.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/raw-multiline.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_138(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/raw.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/raw.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_139(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/simple.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/simple.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_140(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/unicode-escape.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/unicode-escape.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_141(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/unicode-literal.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/unicode-literal.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_142(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/with-pound.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/string/with-pound.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_143(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-implicit-and-explicit-after.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-implicit-and-explicit-after.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_144(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-implicit.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-implicit.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_145(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-many.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-many.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_146(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-nest.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-nest.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_147(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-one.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-one.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_148(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-table-array.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-table-array.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_149(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-within-dotted.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/array-within-dotted.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_150(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/empty-name.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/empty-name.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_151(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/empty.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/empty.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_152(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/keyword.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/keyword.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_153(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/names.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/names.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_154(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/no-eol.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/no-eol.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_155(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/sub-empty.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/sub-empty.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_156(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/sub.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/sub.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_157(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/whitespace.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/whitespace.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_158(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/with-literal-string.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/with-literal-string.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_159(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/with-pound.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/with-pound.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_160(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/with-single-quotes.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/with-single-quotes.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

    def test_161(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/without-super.toml'))) as f_test:
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid/table/without-super.json'))) as f_result:
                correct = convert_dict(json.load(f_result))
                parser.parse(f_test.read())
                test = parser.result
                self.assertEqual(test,correct)

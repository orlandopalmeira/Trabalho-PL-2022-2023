import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import parser

class Tests_spec(unittest.TestCase):

    def test_000(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_001(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_002(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-of-tables-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-of-tables-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_003(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-of-tables-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-of-tables-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_004(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-of-tables-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/array-of-tables-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_005(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/boolean-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/boolean-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_006(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/comment-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/comment-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_007(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/float-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/float-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_008(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/float-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/float-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_009(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/float-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/float-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_010(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/inline-table-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/inline-table-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_011(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/inline-table-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/inline-table-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_012(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/inline-table-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/inline-table-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_013(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/inline-table-3.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/inline-table-3.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_014(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/integer-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/integer-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_015(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/integer-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/integer-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_016(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/integer-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/integer-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_017(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/key-value-pair-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/key-value-pair-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_018(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_019(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_020(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-3.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-3.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_021(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-4.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-4.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_022(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-5.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-5.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_023(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-6.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-6.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_024(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-7.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/keys-7.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_025(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/local-date-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/local-date-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_026(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/local-date-time-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/local-date-time-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_027(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/local-time-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/local-time-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_028(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/offset-date-time-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/offset-date-time-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_029(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/offset-date-time-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/offset-date-time-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_030(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_031(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_032(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_033(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-3.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-3.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_034(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-4.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-4.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_035(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-5.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-5.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_036(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-6.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-6.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_037(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-7.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/string-7.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_038(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-0.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-0.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_039(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-1.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-1.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_040(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_041(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-3.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-3.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_042(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-4.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-4.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_043(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-5.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-5.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_044(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-6.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-6.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_045(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-7.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-7.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_046(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-8.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-8.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_047(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-9.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/spec/table-9.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
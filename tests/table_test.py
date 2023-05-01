import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import Parser

myparser = Parser()

class Tests_table(unittest.TestCase):

    def test_000(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-implicit-and-explicit-after.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-implicit-and-explicit-after.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_001(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-implicit.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-implicit.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_002(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-many.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-many.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_003(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-nest.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-nest.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_004(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-one.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-one.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_005(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-table-array.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-table-array.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_006(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-within-dotted.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/array-within-dotted.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_007(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/empty-name.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/empty-name.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_008(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/empty.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/empty.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_009(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/keyword.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/keyword.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_010(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/no-eol.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/no-eol.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_011(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/sub-empty.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/sub-empty.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_012(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/sub.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/sub.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_013(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/whitespace.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/whitespace.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_014(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/with-literal-string.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/with-literal-string.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_015(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/with-pound.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/with-pound.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_016(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/with-single-quotes.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/with-single-quotes.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_017(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/without-super.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/table/without-super.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
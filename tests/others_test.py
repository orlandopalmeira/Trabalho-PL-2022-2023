import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import Parser

myparser = Parser()

class Tests_others(unittest.TestCase):

    def test_000(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/empty-file.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/empty-file.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_001(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/example.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/example.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_002(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/implicit-and-explicit-after.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/implicit-and-explicit-after.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_003(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/implicit-and-explicit-before.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/implicit-and-explicit-before.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_004(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/implicit-groups.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/implicit-groups.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_005(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/newline-crlf.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/newline-crlf.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_006(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/newline-lf.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/newline-lf.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_007(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/spec-example-1-compact.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/spec-example-1-compact.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_008(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/spec-example-1.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/others/spec-example-1.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
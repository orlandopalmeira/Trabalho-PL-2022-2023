import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import parser

class Tests_inline-table(unittest.TestCase):

    def test_000(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/array.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/array.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_001(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/bool.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/bool.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_002(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/empty.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/empty.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_003(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/end-in-bool.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/end-in-bool.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_004(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/inline-table.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/inline-table.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_005(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/key-dotted.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/key-dotted.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_006(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/multiline.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/multiline.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_007(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/nest.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/inline-table/nest.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
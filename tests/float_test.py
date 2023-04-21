import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import parser

class Tests_float(unittest.TestCase):

    def test_000(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/exponent.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/exponent.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_001(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/float.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/float.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_002(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/inf-and-nan.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/inf-and-nan.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_003(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/long.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/long.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_004(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/underscore.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/underscore.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_005(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/zero.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/float/zero.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
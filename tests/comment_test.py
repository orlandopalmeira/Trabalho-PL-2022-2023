import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import parser

class Tests_comment(unittest.TestCase):

    def test_000(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/at-eof.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/at-eof.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_001(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/at-eof2.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/at-eof2.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_002(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/everywhere.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/everywhere.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_003(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/noeol.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/noeol.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_004(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/nonascii.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/nonascii.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
    def test_005(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/tricky.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/comment/tricky.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
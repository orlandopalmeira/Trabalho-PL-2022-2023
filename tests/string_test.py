import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import Parser

myparser = Parser()

class Tests_string(unittest.TestCase):

    def test_000(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/double-quote-escape.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/double-quote-escape.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_001(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/empty.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/empty.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_002(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/escape-tricky.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/escape-tricky.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_003(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/escaped-escape.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/escaped-escape.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_004(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/escapes.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/escapes.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_005(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/multiline-escaped-crlf.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/multiline-escaped-crlf.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_006(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/multiline-quotes.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/multiline-quotes.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_007(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/nl.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/nl.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_008(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/raw-multiline.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/raw-multiline.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_009(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/raw.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/raw.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_010(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/simple.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/simple.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_011(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/unicode-escape.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/unicode-escape.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
    def test_012(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/with-pound.toml'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/string/with-pound.json'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        
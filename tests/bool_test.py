import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import parser

class Tests_bool(unittest.TestCase):

    def test_000(self):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/bool/bool.toml'))) as f_test:
            parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', './valid2/bool/bool.json'))) as f_result:
            correct = json.load(f_result)
        test = parser.result
        self.assertEqual(test,correct)
        
valid1 = [
    ('./valid2/array/array.toml', './valid2/array/array.json'),
    ('./valid2/array/bool.toml', './valid2/array/bool.json'),
    ('./valid2/array/empty.toml', './valid2/array/empty.json'),
    ('./valid2/array/hetergeneous.toml', './valid2/array/hetergeneous.json'),
    ('./valid2/array/mixed-int-array.toml', './valid2/array/mixed-int-array.json'),
    ('./valid2/array/mixed-int-float.toml', './valid2/array/mixed-int-float.json'),
    ('./valid2/array/mixed-int-string.toml', './valid2/array/mixed-int-string.json'),
    ('./valid2/array/mixed-string-table.toml', './valid2/array/mixed-string-table.json'),
    ('./valid2/array/nested-double.toml', './valid2/array/nested-double.json'),
    ('./valid2/array/nested-inline-table.toml', './valid2/array/nested-inline-table.json'),
    ('./valid2/array/nested.toml', './valid2/array/nested.json'),
    ('./valid2/array/nospaces.toml', './valid2/array/nospaces.json'),
    ('./valid2/array/string-quote-comma-2.toml', './valid2/array/string-quote-comma-2.json'),
    ('./valid2/array/string-quote-comma.toml', './valid2/array/string-quote-comma.json'),
    ('./valid2/array/string-with-comma-2.toml', './valid2/array/string-with-comma-2.json'),
    ('./valid2/array/string-with-comma.toml', './valid2/array/string-with-comma.json'),
    ('./valid2/array/strings.toml', './valid2/array/strings.json'),
    ('./valid2/array/table-array-string-backslash.toml', './valid2/array/table-array-string-backslash.json')
]

valid2 = [
    ('./valid2/bool/bool.toml', './valid2/bool/bool.json')
]

valid3 = [
    ('./valid2/comment/at-eof.toml', './valid2/comment/at-eof.json'),
    ('./valid2/comment/at-eof2.toml', './valid2/comment/at-eof2.json'),
    ('./valid2/comment/everywhere.toml', './valid2/comment/everywhere.json'),
    ('./valid2/comment/noeol.toml', './valid2/comment/noeol.json'),
    ('./valid2/comment/nonascii.toml', './valid2/comment/nonascii.json'),
    ('./valid2/comment/tricky.toml', './valid2/comment/tricky.json')
]

valid4 = [
    ('./valid2/datetime/datetime.toml', './valid2/datetime/datetime.json'),
    ('./valid2/datetime/local-date.toml', './valid2/datetime/local-date.json'),
    ('./valid2/datetime/local-time.toml', './valid2/datetime/local-time.json'),
    ('./valid2/datetime/local.toml', './valid2/datetime/local.json'),
    ('./valid2/datetime/milliseconds.toml', './valid2/datetime/milliseconds.json'),
    ('./valid2/datetime/timezone.toml', './valid2/datetime/timezone.json')
]

valid5 = [   
    ('./valid2/float/exponent.toml', './valid2/float/exponent.json'),
    ('./valid2/float/float.toml', './valid2/float/float.json'),
    ('./valid2/float/long.toml', './valid2/float/long.json'),
    ('./valid2/float/underscore.toml', './valid2/float/underscore.json'),
    ('./valid2/float/zero.toml', './valid2/float/zero.json'),
    # ('./valid2/float/inf-and-nan.toml', './valid2/float/inf-and-nan.json')
    ]

valid6 = [
    ('./valid2/inline-table/array.toml', './valid2/inline-table/array.json'),
    ('./valid2/inline-table/bool.toml', './valid2/inline-table/bool.json'),
    ('./valid2/inline-table/empty.toml', './valid2/inline-table/empty.json'),
    ('./valid2/inline-table/end-in-bool.toml', './valid2/inline-table/end-in-bool.json'),
    ('./valid2/inline-table/inline-table.toml', './valid2/inline-table/inline-table.json'),
    ('./valid2/inline-table/key-dotted.toml', './valid2/inline-table/key-dotted.json'),
    ('./valid2/inline-table/multiline.toml', './valid2/inline-table/multiline.json'),
    ('./valid2/inline-table/nest.toml', './valid2/inline-table/nest.json')
]

valid7 = [
    ('./valid2/integer/integer.toml', './valid2/integer/integer.json'),
    ('./valid2/integer/literals.toml', './valid2/integer/literals.json'),
    ('./valid2/integer/long.toml', './valid2/integer/long.json'),
    ('./valid2/integer/underscore.toml', './valid2/integer/underscore.json'),
    ('./valid2/integer/zero.toml', './valid2/integer/zero.json')
]

valid8 = [
    ('./valid2/key/alphanum.toml', './valid2/key/alphanum.json'),
    # ('./valid2/key/case-sensitive.toml', './valid2/key/case-sensitive.json'), # unicode
    ('./valid2/key/dotted-empty.toml', './valid2/key/dotted-empty.json'),
    ('./valid2/key/dotted.toml', './valid2/key/dotted.json'),
    ('./valid2/key/empty.toml', './valid2/key/empty.json'),
    ('./valid2/key/equals-nospace.toml', './valid2/key/equals-nospace.json'),
    ('./valid2/key/escapes.toml', './valid2/key/escapes.json'),
    ('./valid2/key/numeric-dotted.toml', './valid2/key/numeric-dotted.json'),
    ('./valid2/key/numeric.toml', './valid2/key/numeric.json'),
    ('./valid2/key/quoted-dots.toml', './valid2/key/quoted-dots.json'),
    # ('./valid2/key/quoted-unicode.toml', './valid2/key/quoted-unicode.json'), # unicode
    ('./valid2/key/space.toml', './valid2/key/space.json'),
    ('./valid2/key/special-chars.toml', './valid2/key/special-chars.json'),
    ('./valid2/key/special-word.toml', './valid2/key/special-word.json')
]

valid9 = [
    ('./valid2/spec/array-0.toml', './valid2/spec/array-0.json'),
    ('./valid2/spec/array-1.toml', './valid2/spec/array-1.json'),
    ('./valid2/spec/array-of-tables-0.toml', './valid2/spec/array-of-tables-0.json'),
    ('./valid2/spec/array-of-tables-1.toml', './valid2/spec/array-of-tables-1.json'),
    ('./valid2/spec/array-of-tables-2.toml', './valid2/spec/array-of-tables-2.json'),
    ('./valid2/spec/boolean-0.toml', './valid2/spec/boolean-0.json'),
    ('./valid2/spec/comment-0.toml', './valid2/spec/comment-0.json'),
    ('./valid2/spec/float-0.toml', './valid2/spec/float-0.json'),
    ('./valid2/spec/float-1.toml', './valid2/spec/float-1.json'),
    ('./valid2/spec/inline-table-0.toml', './valid2/spec/inline-table-0.json'),
    ('./valid2/spec/inline-table-1.toml', './valid2/spec/inline-table-1.json'),
    ('./valid2/spec/inline-table-2.toml', './valid2/spec/inline-table-2.json'),
    ('./valid2/spec/inline-table-3.toml', './valid2/spec/inline-table-3.json'),
    ('./valid2/spec/integer-0.toml', './valid2/spec/integer-0.json'),
    ('./valid2/spec/integer-1.toml', './valid2/spec/integer-1.json'),
    ('./valid2/spec/integer-2.toml', './valid2/spec/integer-2.json'),
    ('./valid2/spec/key-value-pair-0.toml', './valid2/spec/key-value-pair-0.json'),
    ('./valid2/spec/keys-0.toml', './valid2/spec/keys-0.json'),
    # ('./valid2/spec/keys-1.toml', './valid2/spec/keys-1.json'), # unicode
    ('./valid2/spec/keys-3.toml', './valid2/spec/keys-3.json'),
    ('./valid2/spec/keys-4.toml', './valid2/spec/keys-4.json'),
    ('./valid2/spec/keys-5.toml', './valid2/spec/keys-5.json'),
    ('./valid2/spec/keys-6.toml', './valid2/spec/keys-6.json'),
    ('./valid2/spec/keys-7.toml', './valid2/spec/keys-7.json'),
    ('./valid2/spec/local-date-0.toml', './valid2/spec/local-date-0.json'),
    ('./valid2/spec/local-date-time-0.toml', './valid2/spec/local-date-time-0.json'),
    ('./valid2/spec/local-time-0.toml', './valid2/spec/local-time-0.json'),
    ('./valid2/spec/offset-date-time-0.toml', './valid2/spec/offset-date-time-0.json'),
    ('./valid2/spec/offset-date-time-1.toml', './valid2/spec/offset-date-time-1.json'),
    ('./valid2/spec/string-0.toml', './valid2/spec/string-0.json'),
    ('./valid2/spec/string-1.toml', './valid2/spec/string-1.json'),
    ('./valid2/spec/string-2.toml', './valid2/spec/string-2.json'),
    ('./valid2/spec/string-3.toml', './valid2/spec/string-3.json'),
    ('./valid2/spec/string-4.toml', './valid2/spec/string-4.json'),
    ('./valid2/spec/string-5.toml', './valid2/spec/string-5.json'),
    ('./valid2/spec/string-6.toml', './valid2/spec/string-6.json'),
    ('./valid2/spec/string-7.toml', './valid2/spec/string-7.json'),
    ('./valid2/spec/table-0.toml', './valid2/spec/table-0.json'),
    ('./valid2/spec/table-1.toml', './valid2/spec/table-1.json'),
    ('./valid2/spec/table-2.toml', './valid2/spec/table-2.json'),
    # ('./valid2/spec/table-3.toml', './valid2/spec/table-3.json'), # unicode
    ('./valid2/spec/table-4.toml', './valid2/spec/table-4.json'),
    ('./valid2/spec/table-5.toml', './valid2/spec/table-5.json'),
    ('./valid2/spec/table-6.toml', './valid2/spec/table-6.json'),
    ('./valid2/spec/table-7.toml', './valid2/spec/table-7.json'),
    ('./valid2/spec/table-8.toml', './valid2/spec/table-8.json'),
    ('./valid2/spec/table-9.toml', './valid2/spec/table-9.json'),
    # ('./valid2/spec/float-2.toml', './valid2/spec/float-2.json')
]

valid10 = [
    ('./valid2/string/double-quote-escape.toml', './valid2/string/double-quote-escape.json'),
    ('./valid2/string/empty.toml', './valid2/string/empty.json'),
    ('./valid2/string/escape-tricky.toml', './valid2/string/escape-tricky.json'),
    ('./valid2/string/escaped-escape.toml', './valid2/string/escaped-escape.json'),
    ('./valid2/string/escapes.toml', './valid2/string/escapes.json'),
    ('./valid2/string/multiline-escaped-crlf.toml', './valid2/string/multiline-escaped-crlf.json'),
    ('./valid2/string/multiline-quotes.toml', './valid2/string/multiline-quotes.json'),
    # ('./valid2/string/multiline.toml', './valid2/string/multiline.json'), # unicode
    ('./valid2/string/nl.toml', './valid2/string/nl.json'),
    # ('./valid2/string/quoted-unicode.toml', './valid2/string/quoted-unicode.json'), # unicode
    ('./valid2/string/raw-multiline.toml', './valid2/string/raw-multiline.json'),
    ('./valid2/string/raw.toml', './valid2/string/raw.json'),
    ('./valid2/string/simple.toml', './valid2/string/simple.json'),
    ('./valid2/string/unicode-escape.toml', './valid2/string/unicode-escape.json'),
    # ('./valid2/string/unicode-literal.toml', './valid2/string/unicode-literal.json'), # unicode
    ('./valid2/string/with-pound.toml', './valid2/string/with-pound.json')
]

valid11 = [
    ('./valid2/table/array-implicit-and-explicit-after.toml', './valid2/table/array-implicit-and-explicit-after.json'),
    ('./valid2/table/array-implicit.toml', './valid2/table/array-implicit.json'),
    ('./valid2/table/array-many.toml', './valid2/table/array-many.json'),
    ('./valid2/table/array-nest.toml', './valid2/table/array-nest.json'),
    ('./valid2/table/array-one.toml', './valid2/table/array-one.json'),
    ('./valid2/table/array-table-array.toml', './valid2/table/array-table-array.json'),
    ('./valid2/table/array-within-dotted.toml', './valid2/table/array-within-dotted.json'),
    ('./valid2/table/empty-name.toml', './valid2/table/empty-name.json'),
    ('./valid2/table/empty.toml', './valid2/table/empty.json'),
    ('./valid2/table/keyword.toml', './valid2/table/keyword.json'),
    # ('./valid2/table/names.toml', './valid2/table/names.json'), # unicode
    ('./valid2/table/no-eol.toml', './valid2/table/no-eol.json'),
    ('./valid2/table/sub-empty.toml', './valid2/table/sub-empty.json'),
    ('./valid2/table/sub.toml', './valid2/table/sub.json'),
    ('./valid2/table/whitespace.toml', './valid2/table/whitespace.json'),
    ('./valid2/table/with-literal-string.toml', './valid2/table/with-literal-string.json'),
    ('./valid2/table/with-pound.toml', './valid2/table/with-pound.json'),
    ('./valid2/table/with-single-quotes.toml', './valid2/table/with-single-quotes.json'),
    ('./valid2/table/without-super.toml', './valid2/table/without-super.json')
]

others = [
    ('./valid2/others/empty-file.toml', './valid2/others/empty-file.json'),
    ('./valid2/others/example.toml', './valid2/others/example.json'),
    ('./valid2/others/implicit-and-explicit-after.toml', './valid2/others/implicit-and-explicit-after.json'),
    ('./valid2/others/implicit-and-explicit-before.toml', './valid2/others/implicit-and-explicit-before.json'),
    ('./valid2/others/implicit-groups.toml', './valid2/others/implicit-groups.json'),
    ('./valid2/others/newline-crlf.toml', './valid2/others/newline-crlf.json'),
    ('./valid2/others/newline-lf.toml', './valid2/others/newline-lf.json'),
    ('./valid2/others/spec-example-1-compact.toml', './valid2/others/spec-example-1-compact.json'),
    ('./valid2/others/spec-example-1.toml', './valid2/others/spec-example-1.json'),
]

aux = [
    ('./valid2/array', valid1),
    ('./valid2/bool', valid2),
    ('./valid2/comment',valid3),
    ('./valid2/datetime',valid4),
    ('./valid2/float',valid5),
    ('./valid2/inline-table',valid6),
    ('./valid2/integer',valid7),
    ('./valid2/key',valid8),
    ('./valid2/spec',valid9),
    ('./valid2/string',valid10),
    ('./valid2/table',valid11),
    ('./valid2/others',others)
]

for i,(path,list) in enumerate(aux):
    with open(f'./{path.split("/")[2]}_test.py','w') as f:
        file = f'''import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from grammar import Parser

myparser = Parser()

class Tests_{path.split("/")[2]}(unittest.TestCase):
'''
        for i2,(f1,f2) in enumerate(list):
                file += f'''
    def test_{i2:03d}(self):
        myparser.build()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '{f1}'))) as f_test:
            test = myparser.parser.parse(f_test.read())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '{f2}'))) as f_result:
            correct = json.load(f_result)
        self.assertEqual(test,correct)
        '''
        f.write(file)
'''
Created on Dec 5, 2012

@author: ohad
'''
import unittest

import analyze
import StringIO
import translationese.lexical_variety
import os.path

class TestAnalyze(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        tests_dir = os.path.join(os.path.dirname(__file__), "test_data")
        self.o_dir = os.path.join(tests_dir, "o")
        self.t_dir = os.path.join(tests_dir, "t")

    def assertResultForModule(self, module, expected, variant=None):
        s = StringIO.StringIO()
        analyze.main(module, self.o_dir, self.t_dir, s, variant)
        self.assertMultiLineEqual(expected, s.getvalue())

    def testWithPunctuation(self):
        self.assertResultForModule(translationese.punctuation,
                                   punctuation_result)

    def testWithLexicalVariety(self):
        self.assertResultForModule(translationese.lexical_variety,
                                   lexical_variety_result, 1)

lexical_variety_result = """\
@relation translationese
@attribute 'TTR2' numeric
@attribute class { T, O }

@data
5.23501721729,O
4.96252485208,O
6.0,T
5.16811869688,T
"""

punctuation_result = """\
@relation translationese
@attribute '?' numeric
@attribute '!' numeric
@attribute ':' numeric
@attribute ';' numeric
@attribute '-' numeric
@attribute '(' numeric
@attribute ')' numeric
@attribute '[' numeric
@attribute ']' numeric
@attribute "'" numeric
@attribute '"' numeric
@attribute '/' numeric
@attribute ',' numeric
@attribute '.' numeric
@attribute class { T, O }

@data
0.0005,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,O
0.0005,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,O
0.0005,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,T
0.0005,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,T
"""

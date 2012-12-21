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

    def assertResultForModule(self, module, variant, expected):
        s = StringIO.StringIO()
        analyze.main(module, self.o_dir, self.t_dir, s, variant)
        self.assertMultiLineEqual(expected, s.getvalue())

    def testWithLexicalVariety(self):
        self.assertResultForModule(translationese.lexical_variety, 1, \
                                   lexical_variety_result)

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

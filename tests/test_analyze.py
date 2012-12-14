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
        tests_dir = os.path.join(os.path.dirname(__file__), "test_data")
        self.o_dir = os.path.join(tests_dir, "o")
        self.t_dir = os.path.join(tests_dir, "t")

    def assertResultForModule(self, module, expected):
        s = StringIO.StringIO()
        analyze.main(module, self.o_dir, self.t_dir, s)
        self.assertMultiLineEqual(expected, s.getvalue())

    def testWithLexicalVariety(self):
        self.assertResultForModule(translationese.lexical_variety, \
                                   lexical_variety_result)

lexical_variety_result = """\
@relation translationese
@attribute class { T, O }
@attribute 'type_token_ratio' numeric
@attribute 'log_type_token_ratio' numeric
@attribute 'unique_type_token_ratio' numeric

@data
O,4.28571428571,5.23501721729,659.764332404
O,4.28571428571,4.96252485208,486.477537264
T,6.0,6.0,inf
T,4.8,5.16811869688,643.775164974
"""

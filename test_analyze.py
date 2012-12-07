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
        tests_dir = os.path.join(os.path.dirname(__file__), "tests")
        self.o_dir = os.path.join(tests_dir, "o")
        self.t_dir = os.path.join(tests_dir, "t")

    def assertResultForModule(self, module, expected):
        s = StringIO.StringIO()
        analyze.main(module, self.o_dir, self.t_dir, s)
        self.assertMultiLineEqual(expected, s.getvalue())
        pass

    def testWithLexicalVariety(self):
        self.assertResultForModule(translationese.lexical_variety, \
                                   lexical_variety_result)

lexical_variety_result = """\
@relation translationese
@attribute class { T, O }
@attribute 'type_token_ratio' numeric

@data
O,4.28571428571
O,4.28571428571
T,4.8
T,6.0
"""

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
        os.system("find %s -name '*.analysis' -delete" % tests_dir)

    def assertResultForModule(self, module, expected, variant=None):
        s = StringIO.StringIO()
        analyze.main(module, self.o_dir, self.t_dir, s, variant, timer_stream=None)
        self.assertMultiLineEqual(expected, s.getvalue())

    def testWithPunctuation(self):
        self.assertResultForModule(translationese.contractions,
                                   contractions_result)

    def testWithLexicalVariety(self):
        self.assertResultForModule(translationese.lexical_variety,
                                   lexical_variety_result, 1)

    def testMissingVariant(self):
        def tryToQuantifyWithoutVariant():
            module = translationese.lexical_variety
            analyze.main(module, self.o_dir, self.t_dir)
        self.assertRaises(translationese.MissingVariant, \
                          tryToQuantifyWithoutVariant)

    def testExtraVariant(self):
        def tryToQuantifyWithVariant():
            module = translationese.contractions
            analyze.main(module, self.o_dir, self.t_dir, variant=0)
        self.assertRaises(translationese.NoVariants, \
                          tryToQuantifyWithVariant)

    def testUndefinedVariant(self):
        def tryToQuantifyWithVariant():
            module = translationese.lexical_variety
            analyze.main(module, self.o_dir, self.t_dir, variant=5)
        self.assertRaises(translationese.NoSuchVariant, \
                          tryToQuantifyWithVariant)

lexical_variety_result = """\
@relation translationese
@attribute 'TTR2' numeric
@attribute class { T, O }

@data
4.82532632325,O
4.96252485208,O
6.0,T
5.16811869688,T
"""

contractions_result = """\
@relation translationese
@attribute "can't" numeric
@attribute "couldn't" numeric
@attribute "didn't" numeric
@attribute "doesn't" numeric
@attribute "don't" numeric
@attribute "he'd" numeric
@attribute "he'll" numeric
@attribute "he's" numeric
@attribute "here's" numeric
@attribute "how's" numeric
@attribute "i'd" numeric
@attribute "i'll" numeric
@attribute "i'm" numeric
@attribute "i've" numeric
@attribute "it's" numeric
@attribute "let's" numeric
@attribute "must've" numeric
@attribute "she'd" numeric
@attribute "she'll" numeric
@attribute "she's" numeric
@attribute "should've" numeric
@attribute "there's" numeric
@attribute "they'd" numeric
@attribute "they'll" numeric
@attribute "they're" numeric
@attribute "they've" numeric
@attribute "we'd" numeric
@attribute "we'll" numeric
@attribute "we're" numeric
@attribute "we've" numeric
@attribute "what's" numeric
@attribute "where's" numeric
@attribute "who're" numeric
@attribute "who's" numeric
@attribute "who've" numeric
@attribute "would've" numeric
@attribute "wouldn't" numeric
@attribute "you'd" numeric
@attribute "you'll" numeric
@attribute "you're" numeric
@attribute "you've" numeric
@attribute class { T, O }

@data
0,0.25,0,0,0,0,0,0,0,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,O
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,O
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,T
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,T
"""

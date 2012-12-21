'''
Created on Dec 14, 2012

@author: ohad
'''

import unittest
from translationese import Analysis
from translationese import punctuation

class TestPunctuation(unittest.TestCase):
    def setUp(self):
        self.sentence = """Punctuation: Small, easily-overlooked symbols, which can """ \
                        """completely change the "meaning" of a sentence."""
        self.analysis = Analysis(self.sentence)

    def testVariant1(self):
        result = punctuation.quantify_variant(self.analysis, 0)
        expected = {
                    ':': 1 / 2000.0,
                    ',': 2 / 2000.0,
                    '.': 1 / 2000.0,
                    '"': 2 / 2000.0,
                    }
        self.assertDictContainsSubset(expected, result)

    def testVariant2(self):
        result = punctuation.quantify_variant(self.analysis, 1)
        expected = {
                    ':': 4 * 1 / 19.0,
                    ',': 4 * 2 / 19.0,
                    '.': 4 * 1 / 19.0,
                    '"': 4 * 2 / 19.0,
                    }
        self.assertDictContainsSubset(expected, result)

    def testVariant3(self):
        result = punctuation.quantify_variant(self.analysis, 2)
        expected = {
                    ':': 4 * 1 / 7.0,
                    ',': 4 * 2 / 7.0,
                    '.': 4 * 1 / 7.0,
                    '"': 4 * 2 / 7.0,
                    }
        self.assertDictContainsSubset(expected, result)

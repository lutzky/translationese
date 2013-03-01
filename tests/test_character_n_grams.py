'''
Created on Dec 5, 2012

@author: ohad
'''
import unittest

from translationese import Analysis
from translationese import character_n_grams
from tests.util import SparseDictEqualMixin

class TestCharacterNGrams(SparseDictEqualMixin, unittest.TestCase):
    def setUp(self):
        self.analysis = Analysis("Hello, a world!")
        self.quantify = character_n_grams.quantify_variant

    def testUnigrams(self):
        self.variant = 0
        self.result = self.quantify(self.analysis, self.variant)
        self.expected = {
                "a": 1 / 15.0,
                "h": 1 / 15.0,
                "e": 1 / 15.0,
                "l": 3 / 15.0,
                "o": 2 / 15.0,
                "w": 1 / 15.0,
                "r": 1 / 15.0,
                "d": 1 / 15.0,
                }

        self.assertSparseDictEqual(self.expected, self.result)

    def testBigrams(self):
        self.variant = 1
        self.result = self.quantify(self.analysis, self.variant)
        self.expected = {
                "<h": 1 / 15.0,
                "he": 1 / 15.0,
                "el": 1 / 15.0,
                "ll": 1 / 15.0,
                "lo": 1 / 15.0,
                "o>": 1 / 15.0,
                "<a": 1 / 15.0,
                "a>": 1 / 15.0,
                "<w": 1 / 15.0,
                "wo": 1 / 15.0,
                "or": 1 / 15.0,
                "rl": 1 / 15.0,
                "ld": 1 / 15.0,
                "d>": 1 / 15.0,
                }

        self.assertSparseDictEqual(self.expected, self.result)

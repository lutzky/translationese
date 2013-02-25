'''
Created on Dec 5, 2012

@author: ohad
'''
import unittest

from translationese import Analysis
from translationese import character_n_grams
from translationese.character_n_grams import \
        CharacterNGramAttributeVariantGenerator
from tests.util import SparseDictEqualMixin

class TestCharacterNGramAttributeVariantGenerator(SparseDictEqualMixin,
                                                  unittest.TestCase):
    def setUp(self):
        self.miniAlphabet = ["a", "b", "c"]

    def testUnigrams(self):
        expected = self.miniAlphabet
        generator = CharacterNGramAttributeVariantGenerator(self.miniAlphabet)
        actual = generator[0]

        self.assertEqual(actual, expected)

    def testBigrams(self):
        generator = CharacterNGramAttributeVariantGenerator(self.miniAlphabet)
        actual = generator[1]

        expected = [
                "<a", "<b", "<c",
                "a>", "b>", "c>",
                "aa", "ab", "ac",
                "ba", "bb", "bc",
                "ca", "cb", "cc",
                ]

        self.assertEqual(actual, expected)

    def testTrigrams(self):
        generator = CharacterNGramAttributeVariantGenerator(self.miniAlphabet)
        actual = generator[2]

        expected = [
                "<aa", "<ab", "<ac",
                "<ba", "<bb", "<bc",
                "<ca", "<cb", "<cc",
                "aa>", "ab>", "ac>",
                "ba>", "bb>", "bc>",
                "ca>", "cb>", "cc>",
                "aaa", "aab", "aac",
                "aba", "abb", "abc",
                "aca", "acb", "acc",
                "baa", "bab", "bac",
                "bba", "bbb", "bbc",
                "bca", "bcb", "bcc",
                "caa", "cab", "cac",
                "cba", "cbb", "cbc",
                "cca", "ccb", "ccc",
                ]

        self.assertEqual(actual, expected)

class TestCharacterNGrams(SparseDictEqualMixin, unittest.TestCase):
    def setUp(self):
        self.analysis = Analysis("Hello, world!")
        self.quantify = character_n_grams.quantify_variant

    def testUnigrams(self):
        self.variant = 0
        self.result = self.quantify(self.analysis, self.variant)
        self.expected = {
                "h": 1 / 13.0,
                "e": 1 / 13.0,
                "l": 3 / 13.0,
                "o": 2 / 13.0,
                "w": 1 / 13.0,
                "r": 1 / 13.0,
                "d": 1 / 13.0,
                }

        self.assertSparseDictEqual(self.expected, self.result)

    def testBigrams(self):
        self.variant = 1
        self.result = self.quantify(self.analysis, self.variant)
        self.expected = {
                "<h": 1 / 13.0,
                "he": 1 / 13.0,
                "el": 1 / 13.0,
                "ll": 1 / 13.0,
                "lo": 1 / 13.0,
                "o>": 1 / 13.0,
                "<w": 1 / 13.0,
                "wo": 1 / 13.0,
                "or": 1 / 13.0,
                "rl": 1 / 13.0,
                "ld": 1 / 13.0,
                "d>": 1 / 13.0,
                }

        self.assertSparseDictEqual(self.expected, self.result)

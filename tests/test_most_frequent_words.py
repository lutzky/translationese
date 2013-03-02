import unittest
from translationese import Analysis
from translationese import most_frequent_words
from tests.util import SparseDictEqualMixin

class TestMostFrequentWords(SparseDictEqualMixin, unittest.TestCase):
    sentence = 'The birds, the bees, and that one rabbit.'

    def testVariant0(self):
        a = Analysis(self.sentence)
        expected = {
                    'the': 2 / 11.0,
                    'and': 1 / 11.0,
                    }
        result = most_frequent_words.quantify_variant(a, 0)
        self.assertSparseDictEqual(expected, result)

    def testVariant1(self):
        a = Analysis(self.sentence)
        expected = {
                    'the': 2 / 11.0,
                    'and': 1 / 11.0,
                    'that': 1 / 11.0,
                    }
        result = most_frequent_words.quantify_variant(a, 1)
        self.assertSparseDictEqual(expected, result)

    def testVariant2(self):
            a = Analysis(self.sentence)
            expected = {
                        'the': 2 / 11.0,
                        'and': 1 / 11.0,
                        'that': 1 / 11.0,
                        'one': 1 / 11.0,
                        }
            result = most_frequent_words.quantify_variant(a, 2)
            self.assertSparseDictEqual(expected, result)

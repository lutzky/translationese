import unittest

from translationese import Analysis
from translationese import pos_n_grams
from tests.util import SparseDictEqualMixin

class TestPosNGrams(SparseDictEqualMixin, unittest.TestCase):
    def setUp(self):
        self.analysis = Analysis("We like dogs, and we dislike cats.")

    def testUnigrams(self):
        self.expected = { 
                'PRP': 2,
                'VBP': 2,
                'NNS': 2,
                ',': 1,
                'CC':1,
                '.': 1,
                }
        self.result = pos_n_grams.quantify_variant(self.analysis, 0)

    def testBigrams(self):
        self.expected = {
                'PRP VBP': 2,
                'VBP NNS': 2,
                'NNS ,': 1,
                ', CC': 1,
                'CC PRP': 1,
                'NNS .': 1
                }
        self.result = pos_n_grams.quantify_variant(self.analysis, 1)

    def testTrigrams(self):
        self.expected = {
                'PRP VBP NNS': 2,
                'VBP NNS ,': 1,
                'NNS , CC': 1,
                ', CC PRP': 1,
                'CC PRP VBP': 1,
                'VBP NNS .': 1,
                }

        self.result = pos_n_grams.quantify_variant(self.analysis, 2)

    def tearDown(self):
        self.assertSparseDictEqual(self.expected, self.result)

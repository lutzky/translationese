'''
Created on Jan 15, 2013

@author: Gal Star
'''
import unittest
from translationese import mean_multiple_naming
from translationese import Analysis

class TestMeanMultipleNaming(unittest.TestCase):
    def tearDown(self):
        result = mean_multiple_naming.quantify(self.analysis)
        self.assertDictEqual(self.expected, result)

    def testSimple(self):
        sentence = "Dr James Brown, specialist in physics, visited in Haifa University."""
        self.analysis = Analysis(sentence)
        self.expected = { "mean_multiple_naming": 5.0 / 10.0 }

    def test(self):
        sentence = "St. Patric's Day is a great day."
        self.analysis = Analysis(sentence)
        self.expected = { "mean_multiple_naming": 4.0 / 8.0 }

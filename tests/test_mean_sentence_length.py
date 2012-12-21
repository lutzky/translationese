'''
Created on Dec 21, 2012

@author: Ohad Lutzky
'''
import unittest
from translationese import mean_sentence_length
from translationese import Analysis

class TestMeanSetenceLength(unittest.TestCase):
    def setUp(self):
        self.sentence = "I came.  I saw. I conquered. I didn't elaborate."
        self.analysis = Analysis(self.sentence)

    def testSimple(self):
        expected = { "mean_sentence_length": 3.5 }
        result = mean_sentence_length.quantify(self.analysis)
        self.assertDictEqual(expected, result)

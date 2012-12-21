'''
Created on Dec 21, 2012

@author: Ohad Lutzky
'''
import unittest
from translationese import mean_word_length
from translationese import Analysis

class TestMeanSetenceLength(unittest.TestCase):
    def tearDown(self):
        result = mean_word_length.quantify(self.analysis)
        self.assertDictEqual(self.expected, result)

    def testWithContraction(self):
        sentence = "A little bit overcautious. Don't you think so?"
        self.analysis = Analysis(sentence)
        # Apostrophe in "Don't" doesn't count.
        self.expected = { "mean_word_length": 36.0 / 8.0 }

    def testWithHyphen(self):
        sentence = "I'm a self-made man."
        self.analysis = Analysis(sentence)
        # Apostrophe in "I'm" and hyphen in "self-made" don't count.
        # However, "self-made" counts as one word.
        self.expected = { "mean_word_length": 14.0 / 4.0 }

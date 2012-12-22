'''
Created on Dec 21, 2012

@author: Ohad Lutzky
'''
import unittest
from translationese import threshold_pmi
from translationese import Analysis
import math

class TestThresholdPMI(unittest.TestCase):
    def testSimple(self):
        sentence = "a b a b b"
        # ("b","b") has negative PMI, the other two are positive
        result = threshold_pmi.quantify(Analysis(sentence))
        self.assertEquals(2 / 2000.0, result["threshold_pmi"])

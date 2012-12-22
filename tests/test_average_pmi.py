'''
Created on Dec 21, 2012

@author: Ohad Lutzky
'''
import unittest
from translationese import average_pmi
from translationese import Analysis
import math

class TestAveragePMI(unittest.TestCase):
    def testComplex(self):
        # Regression check. If anything wildly varies, this test will break.  A
        # white-box tests of this is available:
        # tests.test_translationese.Utilities.test_pmi.
        sentence = "Just because you're a Bad Guy doesn't mean you're a... " \
                   "bad guy."
        result = average_pmi.quantify(Analysis(sentence))
        self.assertAlmostEqual(2.30394, result["average_pmi"], 5)

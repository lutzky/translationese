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
        sentence = "Just because you're a Bad Guy doesn't mean you're a " \
                   "bad guy."
        analysis = Analysis(sentence)

        expected_pmi = {
                ('guy', '.'): 2.1439800628174073,
                ("n't", 'mean'): 2.8371272433773522,
                ('does', "n't"): 2.8371272433773522,
                ('guy', 'does'): 2.1439800628174073,
                ('a', 'bad'): 2.1439800628174073,
                ('mean', 'you'): 2.1439800628174073,
                ('bad', 'guy'): 2.1439800628174073,
                ('just', 'because'): 2.8371272433773522,
                ("'re", 'a'): 2.1439800628174073,
                ('because', 'you'): 2.1439800628174073,
                ('you', "'re"): 2.1439800628174073
                }

        self.assertDictEqual(expected_pmi, analysis.pmi())
        average_expected_pmi = sum(expected_pmi.values()) / len(expected_pmi)
        self.assertAlmostEqual(2.33302, average_expected_pmi, 5)
        result = average_pmi.quantify(analysis)
        self.assertAlmostEqual(average_expected_pmi, result["average_pmi"], 5)

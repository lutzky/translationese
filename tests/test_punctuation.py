'''
Created on Dec 14, 2012

@author: ohad
'''

import unittest
from translationese import Analysis
from translationese import punctuation

class TestPunctuation(unittest.TestCase):
    def testSimple(self):
        a = Analysis("""How now, "brown" 'cow'?""")
        expected_normalized = {
                               '?': 1.0 / 2000,
                               "'": 2.0 / 2000,
                               '"': 2.0 / 2000
                               }

        self.assertDictContainsSubset(expected_normalized,
                                      punctuation.quantify(a))

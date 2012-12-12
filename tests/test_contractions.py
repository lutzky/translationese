'''
Created on Dec 11, 2012

@author: Ohad Lutzky
'''
import unittest
from translationese import contractions
from translationese import Analysis

class TestContractions(unittest.TestCase):
    def testContractions(self):
        a = Analysis("I'm certain he said I am later than I am, "
                     "let's go.")
        result = contractions.quantify(a)
        self.assertAlmostEqual(0.5, result["i'm"])
        self.assertAlmostEqual(1.0, result["let's"])
        self.assertEqual(0.0, result["didn't"])

    def testMultiContractions(self):
        a = Analysis("What's the difference between what is shown "
                     "now and what has been shown before?")
        result = contractions.quantify(a)
        self.assertAlmostEqual(0.5, result["what's"])

if __name__ == "__main__":
    unittest.main()

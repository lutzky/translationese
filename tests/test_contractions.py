'''
Created on Dec 11, 2012

@author: Ohad Lutzky
'''
import unittest
from translationese import contractions
import translationese

class TestContractions(unittest.TestCase):
    def testContractions(self):
        a = translationese.Analysis("I'm certain he said I am "
                                    "later than I am usually. Let's go.")
        result = contractions.quantify(a)
        self.assertAlmostEqual(0.5, result["i'm"])
        self.assertAlmostEqual(1.0, result["let's"])

if __name__ == "__main__":
    unittest.main()

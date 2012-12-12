'''
Created on Dec 11, 2012

@author: Ohad Lutzky
'''
import unittest
from translationese import pronouns
import translationese


class TestPronouns(unittest.TestCase):
    def testPronouns(self):
        a = translationese.Analysis("If we are them, then they "
                                    "themselves are us.")
        result = pronouns.quantify(a)
        self.assertAlmostEqual(1.0 / 11.0, result["we"])
        self.assertAlmostEqual(1.0 / 11.0, result["them"])
        self.assertNotIn("are", result)

if __name__ == "__main__":
    unittest.main()

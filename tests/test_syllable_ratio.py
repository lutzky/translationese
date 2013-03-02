import unittest
from translationese import syllable_ratio, Analysis

class TestSyllableRatio(unittest.TestCase):
    def testSyllableRatio(self):
        a = Analysis("A test for vowels and such")
        # 'vowels' counts as having two syllables
        expected = 7 / 6.0
        result = syllable_ratio.quantify(a)["syllable_ratio"]
        self.assertAlmostEqual(expected, result)

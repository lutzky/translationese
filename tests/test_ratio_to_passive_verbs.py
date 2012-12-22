import unittest
from translationese import ratio_to_passive_verbs
import translationese

class RatioToPassiveVerbsTest(unittest.TestCase):
    def test_simple(self):
        expected1 = { "ratio_to_passive_verbs" : 0.0 }
        expected2 = { "ratio_to_passive_verbs" : 0.25 }
        
        a1 = translationese.Analysis("""Tomorrow i will be there to answer your call""")
        a2 = translationese.Analysis("""If It can be bought for less money, I will go and buy it""")
        
        self.assertEqual(expected1, ratio_to_passive_verbs.quantify(a1))
        self.assertEqual(expected2, ratio_to_passive_verbs.quantify(a2))
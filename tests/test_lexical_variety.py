import unittest
from translationese import lexical_variety
import translationese
import math

class TypeTokenRatioTest(unittest.TestCase):
    def test_simple(self):
        a = translationese.Analysis("""Hello hello world world.""")
        quantifier = lexical_variety.LexicalVarietyQuantifier(a)
        self.assertAlmostEqual(6 * (3 / 5.0), quantifier.type_token_ratio(), 1)
        self.assertAlmostEqual(6 * math.log(3) / math.log(5.0),
                               quantifier.log_type_token_ratio(), 1)
        self.assertAlmostEqual(100 * math.log(5.0) / (1 - 1 / 3.0),
                               quantifier.unique_type_token_ratio(), 1)

    def test_infinite_uniqueness(self):
        a = translationese.Analysis("Only different words.")
        quantifier = lexical_variety.LexicalVarietyQuantifier(a)
        self.assertEqual(float("infinity"),
                         quantifier.unique_type_token_ratio())

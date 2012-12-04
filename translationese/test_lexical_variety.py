import unittest
import translationese.lexical_variety

class TypeTokenRatioTest(unittest.TestCase):
    def test_simple(self):
        a = translationese.Analysis("""Hello hello world world""")
        result = translationese.lexical_variety.quantify(a)

        self.assertEqual(0.5, result["type_token_ratio"])

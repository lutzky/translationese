import unittest
import translationese

class TypeTokenRatioTest(unittest.TestCase):
    def test_simple(self):
        s = """Hello hello world world"""

        self.assertEqual(0.5, translationese.type_token_ratio(s))

import unittest
import translationese

class TypeTokenRatioTest(unittest.TestCase):
    def test_simple(self):
        s = """Hello hello world world"""

        self.assertEqual(0.5, translationese.type_token_ratio(s))

class MeanWordLength(unittest.TestCase):
    def test_simple(self):
        s1 = """hello there luzky!"""
        s2 = """is good-will"""

        self.assertEqual(5, translationese.mean_word_length(s1))
        self.assertEqual(5.5, translationese.mean_word_length(s2))

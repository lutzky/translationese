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

class MostFrequentWordsTest(unittest.TestCase):
    def test_simple(self):
        s = "Hello hello hello cruel cruel world"

        self.assertEqual([0.5, 1/3.0, 1/6.0],
                         translationese.most_frequent_words(s, 3))

class AverageSentenceLengthTest(unittest.TestCase):
    def test_simple(self):
        s = "Hello there. How now, brown cow?"
        
        self.assertEquals(4.5, translationese.average_sentence_length(s))
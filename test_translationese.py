import unittest
import translationese

class TypeTokenRatioTest(unittest.TestCase):
    def test_simple(self):
        a = translationese.Analysis("""Hello hello world world""")

        self.assertEqual(0.5, a.type_token_ratio())

class MeanWordLength(unittest.TestCase):
    def test_simple(self):
        a1 = translationese.Analysis("""hello there luzky!""")
        a2 = translationese.Analysis("""is good-will""")

        self.assertEqual(5, a1.mean_word_length())
        self.assertEqual(5.5, a2.mean_word_length())

class MostFrequentWordsTest(unittest.TestCase):
    def test_simple(self):
        a = translationese.Analysis("Hello hello hello cruel cruel world")

        self.assertEqual([0.5, 1/3.0, 1/6.0], a.words_freqs())

class AverageSentenceLengthTest(unittest.TestCase):
    def test_simple(self):
        a = translationese.Analysis("Hello there. How now, brown cow?")

        self.assertEquals(4.5, a.average_sentence_length())
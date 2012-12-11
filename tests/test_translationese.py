import unittest
import translationese

class Histogram(unittest.TestCase):
    def test_simple(self):
        sentence = "How much wood would a woodchuck chuck if a " \
            "woodchuck could chuck wood?"
        a = translationese.Analysis(sentence)
        self.assertEquals(
                          {
                           "how": 1 / 14.0,
                           "much": 1 / 14.0,
                           "wood": 2 / 14.0,
                           "would": 1 / 14.0,
                           "a": 2 / 14.0,
                           "woodchuck": 2 / 14.0,
                           "if": 1 / 14.0,
                           "chuck": 2 / 14.0,
                           "could": 1 / 14.0,
                           "?": 1 / 14.0,
                           },
                          a.histogram_normalized()
                          )

class MeanWordLength(unittest.TestCase):
    def test_simple(self):
        a1 = translationese.Analysis("""hello there luzky!""")
        a2 = translationese.Analysis("""is good-will""")

        self.assertEqual(5, a1.mean_word_length())
        self.assertEqual(5.5, a2.mean_word_length())

class AverageSentenceLengthTest(unittest.TestCase):
    def test_simple(self):
        a = translationese.Analysis("Hello there. How now, brown cow?")

        self.assertEquals(4.5, a.average_sentence_length())

class LexicalDensity(unittest.TestCase):
    def test_simple(self):
        a1 = translationese.Analysis("""we will go tomorrow to see a movie""")
        a2 = translationese.Analysis("""What about punctuation?""")
        
        self.assertEqual(0.5, a1.lexical_density())
        self.assertEqual(3.0/4.0, a2.lexical_density())
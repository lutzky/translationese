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

class Utilities(unittest.TestCase):
    def test_bigrams(self):
        a = translationese.Analysis("Which witch should watch which witch watch?")
        self.assertDictEqual(a.bigrams(),
                             {
                              ("which", "witch"): 2,
                              ("witch", "should"): 1,
                              ("should", "watch"): 1,
                              ("watch", "which"): 1,
                              ("witch", "watch"): 1,
                              ("watch", "?"): 1,
                            })

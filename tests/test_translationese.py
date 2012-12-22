import unittest
import translationese
import math

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

    def test_pmi(self):
        sentence = "a b a b b"
        analysis = translationese.Analysis(sentence)

        # White box test so this can be followed externally

        self.assertDictEqual(analysis.bigrams(), {
            ("a","b"): 2, # freq = 0.5
            ("b","a"): 1, # freq = 0.25
            ("b","b"): 1, # freq = 0.25
            })

        self.assertDictEqual(analysis.histogram_normalized(), {
            "a": 2/5.0,
            "b": 3/5.0,
            })

        expected_pmi = {
                ("a","b"): math.log(0.5 / (2/5.0 * 3/5.0)),
                ("b","a"): math.log(0.25 / (3/5.0 * 2/5.0)),
                ("b","b"): math.log(0.25 / (3/5.0 * 3/5.0)),
                }

        expected_logs = {
                ("a","b"): 0.73397,
                ("b","a"): 0.04082,
                ("b","b"): -0.36464,
                }

        expected_average = sum(expected_logs.values()) / 3.0
        self.assertAlmostEqual(0.13672, expected_average, 5)

        actual_pmi = analysis.pmi()

        for i in expected_pmi.keys():
            self.assertAlmostEqual(expected_pmi[i], expected_logs[i], 5)
            self.assertAlmostEqual(expected_pmi[i], actual_pmi[i], 5)

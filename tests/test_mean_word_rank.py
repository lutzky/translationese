import unittest
from translationese import Analysis
from translationese import mean_word_rank

class TestMeanWordRank(unittest.TestCase):
    def testMeanWordRank(self):
        a = Analysis("Have you not heard? The velociraptor is the word.")

        expected_0 = sum([18, 30, 20, 372, 1, 6000, 8, 1, 250]) / 9.0
        expected_1 = sum([18, 30, 20, 372, 1, 8, 1, 250]) / 8.0

        result_0 = mean_word_rank.quantify_variant(a, 0)["mean_word_rank"]
        result_1 = mean_word_rank.quantify_variant(a, 1)["mean_word_rank"]

        self.assertAlmostEqual(result_0, expected_0)
        self.assertAlmostEqual(result_1, expected_1)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

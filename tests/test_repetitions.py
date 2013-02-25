import unittest
from translationese import Analysis
from translationese import repetitions

class TestRepetitions(unittest.TestCase):
    def testRepetitions(self):
        text = """
        This is a very, very impressive thing. It is more impressive than
        anything I have ever seen. Very good. You have done a fine job.
        """

        # Repeated:
        # very * 3
        # impressive * 2
        # is * 2, but doesn't count.
        # have * 2, but doesn't count.
        # Total: 5

        expected_repetitions = 5
        num_tokens = 30
        expected_result = 3 * float(expected_repetitions) / num_tokens

        a = Analysis(text)
        result = repetitions.quantify(a)
        self.assertAlmostEqual(expected_result, result["repetitions"])

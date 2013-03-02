import unittest
from translationese.positional_token_frequency import quantify
from translationese import Analysis
from util import SparseDictEqualMixin

class TestPositionalTokenFrequency(SparseDictEqualMixin, unittest.TestCase):
    def testPositionalTokenFrequency(self):
        text = """
        Humpty dumpty sat on a wall.
        Humpty dumpty had a great fall.
        Strange occurrence, quite frankly.
        What an egg.
        """

        analysis = Analysis(text)
        
        expected = {
                    "first humpty": 2,
                    "second dumpty": 2,
                    "antepenultimate on": 1,
                    "penultimate a": 1,
                    "last wall": 1,
                    "antepenultimate a": 1,
                    "penultimate great": 1,
                    "last fall": 1,
                    "first strange": 1,
                    "second occurrence": 1,
                    "antepenultimate ,": 1,
                    "penultimate quite": 1,
                    "last frankly": 1,
                    }
        
        result = quantify(analysis)
        
        self.assertSparseDictEqual(expected, result)

import unittest

from translationese import Analysis
from translationese import contextual_function_words
from tests.util import SparseDictEqualMixin

class TestContextualFunctionWords(SparseDictEqualMixin, unittest.TestCase):
    def testContextualFunctionWords(self):
        analysis = Analysis("He better be back, lest a thousand " \
                                 "similarly angry birds show up.")

        expected = {
            'he better be': 1 / 14.0,
            'VBP a thousand': 1 / 14.0,
            'better be back': 1 / 14.0,
            'a thousand similarly': 1 / 14.0,
            'thousand similarly JJ': 1 / 14.0,
        }

        result = contextual_function_words.quantify(analysis)

        self.assertSparseDictEqual(expected, result)

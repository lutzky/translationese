import unittest

class SparseDictEqualMixin(unittest.TestCase):
    """Mixin for testing sparse dictionary equality, where all non-expected
    keys should be 0.0.

    >>> class MyTest(SparseDictEqualMixin, unittest.TestCase):
    ...     def testSomething(self):
    ...         actual = { 'a': 0.0, 'b': 1.0, 'c': 0.0 }
    ...         expected = { 'b': 1.0 }
    ...         self.assertSparseDictEqual(expected, result)
    """
    def assertSparseDictEqual(self, expected, result):
        result_without_zeroes = result.copy()

        for key, value in result_without_zeroes.items():
            if not value: del result_without_zeroes[key]

        self.assertDictEqual(result_without_zeroes, expected)

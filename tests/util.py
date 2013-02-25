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
        expected_with_zeroes = expected.copy()
        for key in result.keys():
            expected_with_zeroes.setdefault(key, 0.0)

        self.assertDictEqual(result, expected_with_zeroes)

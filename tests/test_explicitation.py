'''
Created on Feb 23, 2013

@author: Ohad Lutzky
'''

import unittest
from translationese import explicit_naming
from translationese import single_naming
from translationese import Analysis

class TestExplicitation(unittest.TestCase):
    def testExplicitNaming(self):
        a = Analysis("She and he are better than John, Marie and Jim.")
        result = explicit_naming.quantify(a)
        self.assertAlmostEqual(3.0 * (2.0 / 3.0), result["explicit_naming"])

    def testSingleNaming(self):
        a = Analysis("Jim, George and Bob are my friends. John Doe is not.")
        result = single_naming.quantify(a)
        self.assertAlmostEqual(3.0 / 14.0, result["single_naming"])

if __name__ == "__main__":
    unittest.main()

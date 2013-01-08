import unittest
import translationese.cohesive_markers

sentence = "even if a cat is happy, it will look mad because it is a cat"

class TestCohesiveMarkers(unittest.TestCase):
    def setUp(self):
        self.analysis = translationese.Analysis(sentence)
        self.double_analysis = translationese.Analysis(sentence + \
                                                       " " + sentence)
        self.result = translationese.cohesive_markers.quantify(self.analysis)
        self.double_result = translationese.cohesive_markers.quantify(self.double_analysis)

    def testBecause(self):
        self.assertEquals(1 / 16.0, self.result["because"])
        self.assertEquals(1 / 16.0, self.double_result["because"])
        
    def testAsTo(self):
        self.assertEquals(1 / 11.0, self.result["even if"])
        self.assertEquals(1 / 11.0, self.double_result["even if"])
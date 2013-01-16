import unittest
import translationese.cohesive_markers

sentence = "even if a cat is happy, it will look mad because it is a cat"
sentence2 = "On the other hand On the other hand because"
double_sentence = "%s %s" % ((sentence,) * 2)


class TestCohesiveMarkers(unittest.TestCase):
    def setUp(self):
        self.analysis1 = translationese.Analysis(sentence)
        self.analysis2 = translationese.Analysis(sentence2)
        self.double_analysis = translationese.Analysis(double_sentence)
        self.result1 = translationese.cohesive_markers.quantify(self.analysis1)
        self.result2 = translationese.cohesive_markers.quantify(self.analysis2)
        self.double_result = translationese.cohesive_markers.quantify(self.double_analysis)

    def testBecause(self):
        self.assertEquals(1 / 16.0, self.result1["because"])
        self.assertEquals(1 / 16.0, self.double_result["because"])
        
    def testEvenIf(self):
        self.assertEquals(1 / 16.0, self.result1["even if"])
        self.assertEquals(1 / 16.0, self.double_result["even if"])
    
    def testOnTheOtherHand(self):
        self.assertEquals(2 / 9.0, self.result2["on the other hand"])
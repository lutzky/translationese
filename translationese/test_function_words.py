import unittest
import translationese.function_words

sentence = "The quick brown fox jumped over the lazy dog."

class TestFunctionWords(unittest.TestCase):
    def setUp(self):
        self.analysis = translationese.Analysis(sentence)
        self.double_analysis = translationese.Analysis(sentence + \
                                                       " " + sentence)
        self.result = translationese.function_words.quantify(self.analysis)
        self.double_result = translationese.function_words.quantify(self.double_analysis)

    def testThe(self):
        self.assertEquals(2 / 10.0, self.result["the"])
        self.assertEquals(2 / 10.0, self.double_result["the"])

    def testOver(self):
        self.assertEquals(1 / 10.0, self.result["over"])
        self.assertEquals(1 / 10.0, self.double_result["over"])

import unittest
from translationese import lexical_density
import translationese

class LexcialDensityTest(unittest.TestCase):
    def test_simple(self):
        a1 = translationese.Analysis("""Hello hello world world""")
        a2 = translationese.Analysis("""I'm certain he said I am later than I am, 
                                     let's go""")
        a3 = translationese.Analysis("""we will go tomorrow to see a movie""")
        a4 = translationese.Analysis("""What about punctuation?""")
        
        self.assertEqual(0.0, lexical_density.quantify(a1))
        self.assertEqual((7.0)/(15.0), lexical_density.quantify(a2))
        self.assertEqual(0.5, lexical_density.quantify(a3))
        self.assertEqual(3.0/4.0, lexical_density.quantify(a4))

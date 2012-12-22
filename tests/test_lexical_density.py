import unittest
from translationese import lexical_density
import translationese

class LexcialDensityTest(unittest.TestCase):
    def test_simple(self):
        expected1 = {"lexical_density" : (7.0) / (15.0)}
        expected2 = {"lexical_density" : 0.5 }
        expected3 = {"lexical_density" : (3.0) / (4.0) }
        
        a1 = translationese.Analysis("""I'm certain he said I am later than I am, 
                                     let's go""")
        a2 = translationese.Analysis("""we will go tomorrow to see a movie""")
        a3 = translationese.Analysis("""What about punctuation?""")
        
        self.assertEqual(expected1, lexical_density.quantify(a1))
        self.assertEqual(expected2, lexical_density.quantify(a2))
        self.assertEqual(expected3, lexical_density.quantify(a3))
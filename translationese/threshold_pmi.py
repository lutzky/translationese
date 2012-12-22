"""\
Implementation of Threshold PMI hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.3 Normalization, Threshold PMI
"""

import math
import translationese

attributes = "threshold_pmi"

def quantify(analysis):
    pmi = analysis.pmi()
    positive_pmi = [ x for x in pmi.values() if x > 0 ]
    normalized_result = len(positive_pmi) / 2000.0
    return { "threshold_pmi": normalized_result }

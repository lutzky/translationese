"""\
Implementation of Threshold PMI hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.3 Normalization, Threshold PMI
"""

import math
import translationese

def quantify(analysis):
    pmi = analysis.pmi()
    positive_pmi = [ x for x in pmi.values() if x > 0 ]
    normalized_result = len(positive_pmi) / translationese.expected_chunk_size
    return { "threshold_pmi": normalized_result }

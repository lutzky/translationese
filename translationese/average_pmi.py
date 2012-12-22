"""\
Implementation of Average PMI hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.3 Normalization, Average PMI
"""

import math

attributes = "average_pmi"

def quantify(analysis):
    pmi = analysis.pmi()
    return { "average_pmi": sum(pmi.values()) / len(pmi) }

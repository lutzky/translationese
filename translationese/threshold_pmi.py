"""\
We compute the PMI (see :func:`translationese.Analysis.pmi`) of each bigram in
a chunk, and count the (normalized) number of bigrams with PMI above 0.
"""

import math
import translationese

def quantify(analysis):
    """Quantify threshold PMI"""
    pmi = analysis.pmi()
    positive_pmi = [ x for x in pmi.values() if x > 0 ]
    normalized_result = len(positive_pmi) / translationese.expected_chunk_size
    return { "threshold_pmi": normalized_result }

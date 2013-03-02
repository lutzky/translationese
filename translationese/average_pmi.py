"""\
We expect original texts to use more collocations, and in any case to use them
differently than translated texts. This hypothesis assumes that translations
overuse highly associated words. We therefore use as a feature the average PMI
(see :func:`translationese.Analysis.pmi`) of all bigrams in the chunk.
"""

import math

def quantify(analysis):
    """Quantify average PMI"""
    pmi = analysis.pmi()
    return { "average_pmi": sum(pmi.values()) / len(pmi) }

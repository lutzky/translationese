"""\
The normalized frequencies of the `N` most frequent words in the corpus.
Punctuation marks are excluded.
"""
import translationese
from translationese import word_ranks

VARIANTS = [0, 1, 2]
"""Possible variants.

0. `N` = 5
1. `N` = 10
2. `N` = 50
"""

def quantify_variant(analysis, variant):
    """Quantify most frequent words"""
    assert isinstance(analysis, translationese.Analysis)

    num_top_words = [5, 10, 50]
    d = {}

    for word in word_ranks.TOP_WORDS[:num_top_words[variant]]:
        d[word] = 0

    for token in analysis.tokens():
        if token in d:
            d[token] += 1

    return {k: float(v) / len(analysis.tokens()) for (k, v) in d.items()}

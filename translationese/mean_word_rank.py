"""\
We assume that less frequent words are used more often in original texts than
in translated ones.
"""

import translationese
from translationese.word_ranks import WORD_RANKS

VERY_HIGH_RANK = 6000
"""Very high rank for a word, guessed for unknown words. The highest rank
for known words is 5000."""

VARIANTS = [0, 1]
"""Possible variants for this hypothesis.

0. Words not in this list are given a unique highest rank of ``VERY_HIGH_RANK``.

1. Words not in the list are ignored altogether.
"""

def quantify_variant(analysis, variant):
    """Quantify mean word rank."""
    assert isinstance(analysis, translationese.Analysis)

    count = 0
    rank_sum = 0

    for word in analysis.tokens():
        if not word.isalpha():
            continue

        if word in WORD_RANKS:
            rank_sum += WORD_RANKS[word]
            count += 1
        else:
            if variant == 0:
                rank_sum += VERY_HIGH_RANK
                count += 1
            else:
                pass

    return { "mean_word_rank": float(rank_sum) / count }

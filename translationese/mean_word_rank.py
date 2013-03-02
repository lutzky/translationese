"""\
Implementation of Mean Word Rank hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.1 Simplification, Mean Word Rank
"""
import translationese
from translationese.word_ranks import WORD_RANKS

VERY_HIGH_RANK = 6000

VARIANTS = [0, 1] #: Possible variants

def quantify_variant(analysis, variant):
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

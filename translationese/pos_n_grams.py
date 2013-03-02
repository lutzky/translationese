"""\
We hypothesize that different grammatical structures used
in the different source languages interfere with the translations; and
that translations have unique grammatical structure. We model this
assumption by defining as features unigrams, bigrams and trigrams of
POS tags.
"""

from translationese.utils import output_filter_ngram, sparse_dict_increment

import os
if os.environ.get("READTHEDOCS", None) != 'True':
    from nltk.util import ingrams

VARIANTS = [0, 1, 2] #: Possible variants (unigrams, bigrams, trigrams)

def quantify_variant(analysis, variant):
    """Quantify POS n-grams"""
    n = variant + 1

    d = {}

    all_pos_tags = [ pos for (_, pos) in analysis.pos_tags() ]

    for ngram in ingrams(all_pos_tags, n):
        sparse_dict_increment(d, ngram)

    return {output_filter_ngram(k): v for (k, v) in d.items()}

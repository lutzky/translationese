"""\
Implementation of Interference hypothesis.
Origin
"""

from translationese.utils import output_filter_ngram, sparse_dict_increment
from nltk.util import ingrams

def quantify_variant(analysis, variant):
    n = variant + 1

    d = {}

    all_pos_tags = [ pos for (_, pos) in analysis.pos_tags() ]

    for ngram in ingrams(all_pos_tags, n):
        sparse_dict_increment(d, ngram)

    return {output_filter_ngram(k): v for (k, v) in d.items()}

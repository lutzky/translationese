"""\
Implementation of Interference hypothesis.
Origin
"""

from translationese.utils import output_filter_ngram
from nltk.util import ingrams

def quantify_variant(analysis, variant):
    n = variant + 1

    d = {}

    all_pos_tags = [ pos for (token, pos) in analysis.pos_tags() ]

    for ngram in ingrams(all_pos_tags, n):
        d[ngram] = d.get(ngram, 0) + 1

    return {output_filter_ngram(k): v for (k, v) in d.items()}

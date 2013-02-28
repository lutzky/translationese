"""\
Implementation of Interference hypothesis.
Origin
"""

from translationese.utils import possible_tags, set_cartesian_power, \
    output_filter_ngram
from nltk.util import ingrams

def quantify_variant(analysis, variant):
    n = variant + 1

    d = { output_filter_ngram(ngram): 0
          for ngram in set_cartesian_power(possible_tags, n)}

    all_pos_tags = [ pos for (token, pos) in analysis.pos_tags() ]
    print set(all_pos_tags)

    for ngram in ingrams(all_pos_tags, n):
        d[output_filter_ngram(ngram)] += 1

    return d

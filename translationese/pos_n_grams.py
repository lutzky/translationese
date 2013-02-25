"""\
Implementation of Interference hypothesis.
Origin
"""

import itertools
import sys

possible_tags = [
    "$", "''", "(", ")", ",", "--", ".", ":", "CC", "CD", "DT", "EX", "FW",
    "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNP", "NNPS", "NNS", "PDT",
    "POS", "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB",
    "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB", "``", 
]

def set_cartesian_power(s, n):
    """Returns the set s raised to the power of n; the cartesian product of
    s with itself n times. Returned as an iterator.

    >>> list(set_cartesian_power([1,2,3], 2))
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    """

    sets_to_multiply = [s]*n
    return itertools.product(*sets_to_multiply)

def ngrams(l, n):
    """Returns the set of ngrams from l.

    >>> list(ngrams([1,2,3,4,5], 3))
    [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    """

    l = list(l)

    for i in range(len(l) - n + 1):
        yield tuple(l[i:i+n])

def output_filter_ngram(ngram):
    """Returns the ngram in a form suitable for ARFF output.

    >>> output_filter_ngram(('a','b','c'))
    'a b c'
    """
    return " ".join(ngram)

def quantify_variant(analysis, variant):
    n = variant + 1

    d = { output_filter_ngram(ngram): 0
          for ngram in set_cartesian_power(possible_tags, n)}

    all_pos_tags = ( pos for (token, pos) in analysis.pos_tags() )
    
    for ngram in ngrams(all_pos_tags, n):
        d[output_filter_ngram(ngram)] += 1

    return d

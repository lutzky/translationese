"""\
This feature is a variant of POS n-grams, where the n-grams can be anchored by
specific (function) words. This feature is defined as the (normalized)
frequency of trigrams of function words in the chunk. In addition, we count
also trigrams consisting of two function words (from the same list) and one
other word; in such cases, we replace the other word by its POS. In sum, we
compute the frequencies in the chunk of triplets ``<w1, w2, w3>``, where at
least two of the elements are functions words, and at most one is a POS tag.

See also :mod:`translationese.function_words`.
"""

from translationese.utils import output_filter_ngram, sparse_dict_increment
from translationese.function_words import FUNCTION_WORDS

import os
if os.environ.get("READTHEDOCS", None) != 'True':
    import nltk.util

def function_word_or_POS(token, tag):
    """Returns the given ``token`` if it is a function word, or its POS ``tag``
    otherwise."""
    if token.lower() in FUNCTION_WORDS:
        return token.lower()
    else:
        return tag

def trigram_is_functional(trigram):
    """Returns true iff the given trigram has at least two function words,
    and three words altogether."""
    for w in trigram:
        if not w.isalpha(): return False

    num_function_words = sum(1 for token in trigram if token in FUNCTION_WORDS)
    return num_function_words >= 2

def quantify(analysis):
    """Quantify contextual function words."""
    d = {}

    word_stream = (function_word_or_POS(token, tag) for (token, tag)
                   in analysis.pos_tags())
    num_tokens = float(len(analysis.pos_tags()))

    for trigram in nltk.util.itrigrams(word_stream):
        if trigram_is_functional(trigram):
            sparse_dict_increment(d, trigram)

    return {output_filter_ngram(k): (v / num_tokens) for (k, v) in d.items()}

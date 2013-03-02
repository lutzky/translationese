"""\
We hypothesize that grammatical structure manifests itself in this feature,
and as in POS `n`-grams, the different grammatical structures used in the
different source languages interfere with the translations. We also hypothesize
that this feature captures morphological features of the language. These are
actually three different features (each tested separately): unigrams, bigrams
and trigrams of characters. They are computed similarly to the way POS n-grams
are computed: by the frequencies of `n`-letter occurrences in a chunk,
normalized by the chunk's size. Two special tokens are added to indicate the
beginning and end of each word, in order to properly handle specific word
prefixes and suffixes. We do not capture cross-token character `n`-grams, and
we exclude punctuation marks.
"""

import os
if os.environ.get("READTHEDOCS", None) != 'True':
    from nltk.util import ingrams
from translationese.utils import sparse_dict_increment

__author__ = "Ohad Lutzky"
__email__ = "ohad@lutzky.net"


WORD_START = "<" #: Special token added to start of word
WORD_END = ">" #: Special token added to end of word

VARIANTS = [0, 1, 2] #: Possible variants: Unigrams, bigrams, trigrams

class CharacterNGramQuantifier:
    """Class for quantifying character ``variant``-grams"""
    def __init__(self, variant):
        self.k = variant
        self.histogram = {}

    def __add_token_edges(self, token):
        if len(token) < self.k:
            return
        word_start = WORD_START + token[0:self.k]
        word_end = token[-self.k:] + WORD_END

        for key in word_start, word_end:
            sparse_dict_increment(self.histogram, key)

    def __add_token_ngrams(self, token):
        for current_ngram in ingrams(token, self.k + 1):
            sparse_dict_increment(self.histogram, ''.join(current_ngram))

    def __normalize_histogram(self, analysis):
        factor = 1.0 / len(analysis.fulltext)
        for key in self.histogram.keys():
            self.histogram[key] *= factor

    def quantify(self, analysis):
        """Quantify character `n`-grams."""
        for token in analysis.tokens():
            if not token.isalpha(): continue
            self.__add_token_ngrams(token)
            if self.k > 0:
                self.__add_token_edges(token)

        self.__normalize_histogram(analysis)
        return self.histogram

def quantify_variant(analysis, variant):
    """Quantify character `n`-grams."""
    quantifier = CharacterNGramQuantifier(variant)
    return quantifier.quantify(analysis)

"""\
Implementation of Lexical Variety hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.4 Interference, Character n-Grams
"""

from nltk.util import ingrams
from translationese.utils import sparse_dict_increment

__author__ = "Ohad Lutzky"
__email__ = "ohad@lutzky.net"


WORD_START = "<"
WORD_END = ">"

VARIANTS = [0, 1, 2] #: Possible variants

class CharacterNGramQuantifier:
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
        for token in analysis.tokens():
            if not token.isalpha(): continue
            self.__add_token_ngrams(token)
            if self.k > 0:
                self.__add_token_edges(token)

        self.__normalize_histogram(analysis)
        return self.histogram

def quantify_variant(analysis, variant):
    quantifier = CharacterNGramQuantifier(variant)
    return quantifier.quantify(analysis)

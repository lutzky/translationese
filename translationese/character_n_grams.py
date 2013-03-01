"""\
Implementation of Lexical Variety hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.4 Interference, Character n-Grams
"""

from nltk.util import ingrams

__author__ = "Ohad Lutzky"
__email__ = "ohad@lutzky.net"


WORD_START = "<"
WORD_END = ">"

class CharacterNGramQuantifier:
    def __init__(self, variant, attributes=None):
        self.k = variant

    def __initialize_histogram(self):
        self.histogram = {}

    def __histogram_increment(self, key):
        self.histogram[key] = self.histogram.get(key, 0) + 1

    def __add_token_edges(self, token):
        if len(token) < self.k:
            return
        word_start = WORD_START + token[0:self.k]
        word_end = token[-self.k:] + WORD_END

        for key in word_start, word_end:
            self.__histogram_increment(key)

    def __add_token_ngrams(self, token):
        for current_ngram in ingrams(token, self.k + 1):
            self.__histogram_increment(''.join(current_ngram))

    def __normalize_histogram(self, analysis):
        factor = 1.0 / len(analysis.fulltext)
        for key in self.histogram.keys():
            self.histogram[key] *= factor

    def quantify(self, analysis):
        self.__initialize_histogram()

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

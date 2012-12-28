"""\
Implementation of Lexical Variety hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.4 Interference, Character n-Grams
"""

import string
from itertools import product

__author__ = "Ohad Lutzky"
__email__ = "ohad@lutzky.net"


WORD_START = "<"
WORD_END   = ">"

class CharacterNGramAttributeVariantGenerator:
    def __init__(self, alphabet = string.lowercase):
        self.alphabet = alphabet

    def __getitem__(self, n):
        if n < 0:
            raise IndexError("%d is negative" % n)

        # Variant 0 should produce unigrams, 1 bigrams, etc.
        n += 1

        result = []

        if n > 1:
            alphabet_factors  = [self.alphabet] * (n-1)
            result += product(*([WORD_START] + alphabet_factors))
            result += product(*(alphabet_factors + [WORD_END]))

        alphabets_to_multiply = [self.alphabet] * n
        result += product(*alphabets_to_multiply)

        result = [ "".join(x) for x in result ]
        return result

variant_attributes = CharacterNGramAttributeVariantGenerator()

class CharacterNGramQuantifier:
    def __init__(self, variant, attributes = None):
        if attributes == None:
            generator = CharacterNGramAttributeVariantGenerator()
            attributes = generator[variant]

        self.attributes = attributes

        # k is n - 1. This is useful in all calculations from here.
        self.k = variant

    def __initialize_histogram(self):
        self.histogram = dict([ (x,0) for x in self.attributes ])

    def __histogram_increment(self, key):
        if key in self.histogram:
            self.histogram[key] += 1

    def __add_token_edges(self, token):
        if len(token) < self.k:
            return
        word_start = WORD_START + token[0:self.k]
        word_end = token[-self.k:] + WORD_END

        for key in word_start, word_end:
            self.__histogram_increment(key)

    def __add_token_ngrams(self, token):
        for i in range(self.k, len(token)):
            current_ngram = token[i-self.k : i + 1]
            self.__histogram_increment(current_ngram)

    def __normalize_histogram(self, analysis):
        factor = 1.0 / len(analysis.fulltext)
        for key in self.histogram.keys():
            self.histogram[key] *= factor

    def quantify(self, analysis):
        self.__initialize_histogram()

        for token in analysis.tokens():
            self.__add_token_ngrams(token)
            self.__add_token_edges(token)

        self.__normalize_histogram(analysis)
        return self.histogram

def quantify_variant(analysis, variant):
    quantifier = CharacterNGramQuantifier(variant)
    return quantifier.quantify(analysis)

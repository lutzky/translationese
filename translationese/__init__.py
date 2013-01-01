from memoize import memoize
import nltk
from nltk.tag import pos_tag
import math

expected_chunk_size = 2000.0

def flatten_list(l):
    """Returns a flat list given a list of lists.

    >>> flatten_list([[1,2],[3,4],[5,6]])
    [1, 2, 3, 4, 5, 6]
    """

    return [ item for sublist in l for item in sublist ]

class Analysis(object):
    def __init__(self, obj):
        if isinstance(obj, file):
            self.fulltext = obj.read()
        elif isinstance(obj, str):
            self.fulltext = obj
        else:
            raise AttributeError

    @memoize
    def sentences(self):
        return nltk.sent_tokenize(self.fulltext)

    @memoize
    def case_tokens(self):
        # We tokenize into sentences and then into words due to a warning
        # in the NLTK API doc to only word_tokenize single sentences.
        tokens = []

        for sentence in self.sentences():
            tokens += nltk.word_tokenize(sentence)

        return tokens

    @memoize
    def pos_tags(self):
        list_of_lists = nltk.batch_pos_tag(self.tokenized_sentences())
        return flatten_list(list_of_lists)

    @memoize
    def tokenized_sentences(self):
        sentences = [ s.lower() for s in self.sentences() ]
        return [ nltk.word_tokenize(s) for s in sentences ]

    @memoize
    def tokens(self):
        """Tokens are always in lowercase. For tokens with the original
        case, use case_tokens()."""
        return [ w.lower() for w in self.case_tokens() ]

    @memoize
    def tokens_set(self):
        return set(self.tokens())

    @memoize
    def histogram(self):
        """Return a dictionary { "TOKEN": NUMBER_OF_OCCURENCES, ... }"""
        result = {}
        for t in self.tokens():
            result[t] = result.get(t, 0) + 1
        return result

    @memoize
    def histogram_normalized(self):
        """Returns histogram normalized by number of tokens"""
        items = self.histogram().items()
        num_tokens = float(len(self.tokens()))
        items_normalized = [ (x, y / num_tokens) for x, y in items ]
        return dict(items_normalized)

    @memoize
    def bigrams(self):
        """Return a dictionary { ("w1", "w2"): NUMBER_OF_OCCURENCES, ... }"""
        result = {}
        for i in range(len(self.tokens()) - 1):
            bigram = (self.tokens()[i], self.tokens()[i + 1])
            result[bigram] = result.get(bigram, 0) + 1
        return result

    def pmi(self):
        num_bigrams = float(len(self.tokens()) - 1)
        bigrams_normalized = dict([ (x, y/num_bigrams)
                                    for (x,y) in self.bigrams().items() ])
        freq = self.histogram_normalized()

        bigram_pmi = lambda bigram, bigram_freq: \
                math.log(bigram_freq / (freq[bigram[0]] * freq[bigram[1]]))

        bigram_pmi_pairs = [
                (bigram, bigram_pmi(bigram, bigram_freq))
                for (bigram, bigram_freq) in bigrams_normalized.items()
                ]

        return dict(bigram_pmi_pairs)

import exceptions
class MissingVariant(exceptions.Exception): pass
class NoVariants(exceptions.Exception): pass

class NoSuchVariant(exceptions.Exception):
    def __init__(self, analyzed_module=None):
        if analyzed_module is None:
            Exception.__init__(self, "Invalid variant requested")
            return

        modname = analyzed_module.__name__

        variant_attributes = analyzed_module.variant_attributes
        if isinstance(variant_attributes, list):
            message = "Valid variants for %s are 0..%d" % \
                (modname, len(variant_attributes) - 1)
        elif isinstance(analyzed_module.variant_attributes, dict):
            message = "Valid variants for %s are 0..%d" % \
                (modname, variant_attributes.keys())
        else:
            message = "Invalid variant for module %s" % modname
        Exception.__init__(self, message)

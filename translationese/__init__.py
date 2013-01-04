import memoize
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
    def __init__(self, fulltext = None, stream = None, filename = None):
        self.filename = None
        if fulltext:
            self.fulltext = fulltext
        elif stream:
            self.fulltext = stream.read()
        elif filename:
            self.filename = filename
            self.fulltext = open(filename, "r").read()
            self.picklefile = "%s.analysis" % filename
        else:
            raise AttributeError()

    def __enter__(self):
        self.loadcache()
        return self

    def __exit__(self, type, value, tb):
        if tb is not None:
            # An exception was thrown, do not save pickle
            return False
        self.savecache()

    def loadcache(self):
        if not self.picklefile:
            raise AttributeError('Cannot use Analysis in "with" block '
                                 'unless constructed with a filename.')
        memoize.load(self, self.picklefile)

    def savecache(self):
        memoize.dump(self, self.picklefile)

    @memoize.memoize
    def sentences(self):
        return nltk.sent_tokenize(self.fulltext)

    @memoize.memoize
    def case_tokens(self):
        # We tokenize into sentences and then into words due to a warning
        # in the NLTK API doc to only word_tokenize single sentences.
        tokens = []

        for sentence in self.sentences():
            tokens += nltk.word_tokenize(sentence)

        return tokens

    @memoize.memoize
    def pos_tags(self):
        list_of_lists = nltk.batch_pos_tag(self.tokenized_sentences())
        return flatten_list(list_of_lists)

    @memoize.memoize
    def tokenized_sentences(self):
        sentences = [ s.lower() for s in self.sentences() ]
        return [ nltk.word_tokenize(s) for s in sentences ]

    @memoize.memoize
    def tokens(self):
        """Tokens are always in lowercase. For tokens with the original
        case, use case_tokens()."""
        return [ w.lower() for w in self.case_tokens() ]

    @memoize.memoize
    def tokens_set(self):
        return set(self.tokens())

    @memoize.memoize
    def histogram(self):
        """Return a dictionary { "TOKEN": NUMBER_OF_OCCURENCES, ... }"""
        result = {}
        for t in self.tokens():
            result[t] = result.get(t, 0) + 1
        return result

    @memoize.memoize
    def histogram_normalized(self):
        """Returns histogram normalized by number of tokens"""
        items = self.histogram().items()
        num_tokens = float(len(self.tokens()))
        items_normalized = [ (x, y / num_tokens) for x, y in items ]
        return dict(items_normalized)

    @memoize.memoize
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

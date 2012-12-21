from memoize import memoize
import nltk

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

    def mean_word_length(self):
        real_words = [w for w in self.tokens() if w[0].isalpha()]
        return float(sum([len(w) for w in real_words])) / len(real_words)

    def average_sentence_length(self):
        sentence_length = lambda sentence: len(nltk.word_tokenize(sentence))

        return float(sum([sentence_length(x) for x in self.sentences()])) \
             / len(self.sentences())

    @memoize
    def bigrams(self):
        """Return a dictionary { ("w1", "w2"): NUMBER_OF_OCCURENCES, ... }"""
        result = {}
        for i in range(len(self.tokens()) - 1):
            bigram = (self.tokens()[i], self.tokens()[i + 1])
            result[bigram] = result.get(bigram, 0) + 1
        return result

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

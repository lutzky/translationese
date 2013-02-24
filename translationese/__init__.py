import memoize
import math
import os

if os.environ.get("READTHEDOCS", None) != 'True':
    import nltk
    from nltk.tag import pos_tag

expected_chunk_size = 2000.0

def flatten_list(l):
    """Returns a flat list given a list of lists.

    >>> flatten_list([[1,2],[3,4],[5,6]])
    [1, 2, 3, 4, 5, 6]
    """

    return [ item for sublist in l for item in sublist ]

class Analysis(object):
    """Module to represent and cache an NLTK analysis of a given text. Can
    be initialized either from a file (stream) or fulltext as a parameter."""

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
    def pos_tags_by_sentence(self):
        """Return part-of-speech tags, split by sentence.
        Case-sensitive, as part-of-speech tagging is case-sensitive by nature
        (nouns vs. proper nouns).

        >>> Analysis("I am fine. How are you?").pos_tags_by_sentence()
        ... # doctest: +NORMALIZE_WHITESPACE
        [[('I', 'PRP'), ('am', 'VBP'), ('fine', 'NN'), ('.', '.')],
        [('How', 'WRB'), ('are', 'VBP'), ('you', 'PRP'), ('?', '.')]]
        """
        return nltk.batch_pos_tag(self.case_tokenized_sentences())

    @memoize.memoize
    def pos_tags(self):
        """Return part-of-speech tags, for the entire document.

        >>> Analysis("I am fine. How are you?").pos_tags()
        ... # doctest: +NORMALIZE_WHITESPACE
        [('I', 'PRP'), ('am', 'VBP'), ('fine', 'NN'), ('.', '.'),
        ('How', 'WRB'), ('are', 'VBP'), ('you', 'PRP'), ('?', '.')]
        """
        return flatten_list(self.pos_tags_by_sentence())

    @memoize.memoize
    def tokenized_sentences(self):
        """List of sentences, tokenized as lowercase.

        >>> Analysis("Hello. How are you?").tokenized_sentences()
        [['hello', '.'], ['how', 'are', 'you', '?']]
        """
        lowercase_sentences = [ s.lower() for s in self.sentences() ]
        return [ nltk.word_tokenize(s) for s in lowercase_sentences ]

    @memoize.memoize
    def case_tokenized_sentences(self):
        """List of sentences, tokenized, case-sensitive.

        >>> Analysis("Hello. How are you?").case_tokenized_sentences()
        [['Hello', '.'], ['How', 'are', 'you', '?']]
        """
        return [ nltk.word_tokenize(s) for s in self.sentences() ]

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
    def __init__(self):
        Exception.__init__(self, "Invalid variant requested")

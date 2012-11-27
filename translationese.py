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

    def most_frequent_words(self, n):
        words_freqs = [
                       (t, self.tokens().count(t))
                       for t in self.tokens_set()
                       ]
        words_freqs.sort(key = lambda x: x[1], reverse = True)

        return [ x[1] / float(len(self.tokens()))
                 for x in words_freqs[0:n]]

    def type_token_ratio(self):
        return len(self.tokens_set()) / float(len(self.tokens()))

    def mean_word_length(self):
        real_words = [w for w in self.tokens() if w[0].isalpha()]
        return float(sum([len(w) for w in real_words])) / len(real_words)

    def average_sentence_length(self):
        sentence_length = lambda sentence: len(nltk.word_tokenize(sentence))

        return float(sum([sentence_length(x) for x in self.sentences()])) \
             / len(self.sentences())

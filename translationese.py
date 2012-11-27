from memoize import memoize
import nltk

def makeRegistrar():
    registry = {}
    def registrar(func):
        registry[func.__name__] = func
        return func
    registrar.all = registry
    return registrar

# Create the @translationese_property decorator, so we can collect
# them later.
translationese_property = makeRegistrar()

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
    def words_freqs(self):
        result = [
                       (t, self.tokens().count(t))
                       for t in self.tokens_set()
                       ]
        result.sort(key = lambda x: x[1], reverse = True)

        return [ x[1] / float(len(self.tokens())) for x in result ]

    # FIXME: These need to be auto-generated.
    @translationese_property
    def most_frequent_words_3(self):
        return self.words_freqs()[2]

    @translationese_property
    def most_frequent_words_2(self):
        return self.words_freqs()[1]

    @translationese_property
    def most_frequent_words_1(self):
        return self.words_freqs()[0]

    @translationese_property
    def type_token_ratio(self):
        return len(self.tokens_set()) / float(len(self.tokens()))

    @translationese_property
    def mean_word_length(self):
        real_words = [w for w in self.tokens() if w[0].isalpha()]
        return float(sum([len(w) for w in real_words])) / len(real_words)

    @translationese_property
    def average_sentence_length(self):
        sentence_length = lambda sentence: len(nltk.word_tokenize(sentence))

        return float(sum([sentence_length(x) for x in self.sentences()])) \
             / len(self.sentences())

from memoize import memoize
import nltk
from nltk.tag import pos_tag

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
        return nltk.pos_tag(self.tokens())

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
        """Written by Gal Star"""
        real_words = [w for w in self.tokens() if w[0].isalpha()]
        return float(sum([len(w) for w in real_words])) / len(real_words)

    def average_sentence_length(self):
        sentence_length = lambda sentence: len(nltk.word_tokenize(sentence))

        return float(sum([sentence_length(x) for x in self.sentences()])) \
             / len(self.sentences())

    def lexical_density(self):
        """Written by Gal Star"""
        is_not_verb = lambda letter: letter !='V'
        is_not_noun = lambda letter: letter !='N'
        is_not_adjective = lambda letter: letter !='J'
        is_not_adverb = lambda letter: letter !='R'
        
        is_lexical_density = lambda l: is_not_verb(l) and is_not_noun(l) and \
            is_not_adjective(l) and is_not_adverb(l)
        
        return float(len([x for (x,y) in self.pos_tags() if is_lexical_density(y[0])])) / len(self.tokens())

    @memoize
    def bigrams(self):
        """Return a dictionary { ("w1", "w2"): NUMBER_OF_OCCURENCES, ... }"""
        result = {}
        for i in range(len(self.tokens()) - 1):
            bigram = (self.tokens()[i], self.tokens()[i + 1])
            result[bigram] = result.get(bigram, 0) + 1
        return result


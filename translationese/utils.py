"""Various utilities for translationese analysis"""
import itertools

#: Possible part-of-speech tags
possible_tags = [
    "$", "''", "(", ")", ",", "--", ".", ":", "CC", "CD", "DT", "EX", "FW",
    "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNP", "NNPS", "NNS", "PDT",
    "POS", "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB",
    "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB", "``", 
    "-NONE-",
]

def set_cartesian_power(s, n):
    """Returns the set s raised to the power of n; the cartesian product of
    s with itself n times. Returned as an iterator.

    >>> list(set_cartesian_power([1,2,3], 2))
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    """

    sets_to_multiply = [s]*n
    return itertools.product(*sets_to_multiply)

def ngrams(l, n):
    """Returns the set of ngrams from l.

    >>> list(ngrams([1,2,3,4,5], 3))
    [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    """

    l = list(l)

    for i in range(len(l) - n + 1):
        yield tuple(l[i:i+n])

def output_filter_ngram(ngram):
    """Returns the ngram in a form suitable for ARFF output.

    >>> output_filter_ngram(('a','b','c'))
    'a b c'
    """
    return " ".join(ngram)

def flatten_list(l):
    """Returns a flat list given a list of lists.

    >>> flatten_list([[1,2],[3,4],[5,6]])
    [1, 2, 3, 4, 5, 6]
    """

    return [ item for sublist in l for item in sublist ]

def is_proper_noun(token_tag_pair):
    """Given a pair of a token and a tag, returns True if it represents a
    proper noun.

    >>> import nltk
    >>> nltk.pos_tag(nltk.word_tokenize("Impressive! John defeated Jim!"))
    ... # doctest: +NORMALIZE_WHITESPACE
    [('Impressive', 'JJ'), ('!', 'NN'), ('John', 'NNP'), ('defeated', 'VBD'),
    ('Jim', 'NNP'), ('!', '.')]
    >>> is_proper_noun(('Impressive', 'JJ'))
    False
    >>> is_proper_noun(('John', 'NNP'))
    True
    """

    token, tag = token_tag_pair
    return tag.startswith("NNP")

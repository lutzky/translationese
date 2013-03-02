"""\
This hypothesis checks whether pronouns from
:mod:`translationese.function_words` alone can yield a high classification
accuracy. Each pronoun in the corpus is a feature, whose value is the
normalized frequency of its occurrences in the chunk.
"""

PRONOUNS = [
 "he",
 "her",
 "hers",
 "herself",
 "him",
 "himself",
 "i",
 "it",
 "itself",
 "me",
 "mine",
 "myself",
 "one",
 "oneself",
 "ours",
 "ourselves",
 "she",
 "theirs",
 "them",
 "themselves",
 "they",
 "us",
 "we",
 "you",
 "yourself",
]
"""List of pronouns"""

def quantify(analysis):
    """Quantify pronouns."""
    freq = analysis.histogram_normalized()
    pairs = [ (word, freq.get(word, 0.0)) for word in PRONOUNS ]
    return dict(pairs)

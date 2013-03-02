"""\
We assume that translated texts use simpler words, in particular shorter ones.
Punctuation marks are excluded from the tokens in this feature.  """

import os
if os.environ.get("READTHEDOCS", None) != 'True':
    import nltk

def is_contraction_suffix(token):
    """Is ``token`` a contraction suffix?

    >>> is_contraction_suffix("'s") # let's
    True
    >>> is_contraction_suffix("n't") # don't
    True
    """
    return "'" in token and token.replace("'", "").isalpha()

def is_hyphenated_word(token):
    """Is ``token`` a hyphenated word?

    >>> is_hyphenated_word("ad-hoc")
    True
    """
    return "-" in token and token.replace("-", "").isalpha()

def quantify(analysis):
    """Quantify mean word length."""
    count = 0
    total = 0
    for token in analysis.tokens():
        if token.isalpha():
            count += 1
            total += len(token)
        elif is_hyphenated_word(token):
            count += 1
            # Hyphen doesn't count.
            total += len(token) - 1
        elif is_contraction_suffix(token):
            # It isn't a new word, but it does count as extra characters for
            # the previous one. The apostrophe doens't count though.
            total += len(token) - 1

    return { "mean_word_length": total / float(count) }

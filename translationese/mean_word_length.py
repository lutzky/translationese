"""\
Implementation of Mean Word Length hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.1 Simplification, Mean Word Length
"""

import nltk

def is_contraction_suffix(token):
    return "'" in token and token.replace("'", "").isalpha()

def is_hyphenated_word(token):
    return "-" in token and token.replace("-", "").isalpha()

def quantify(analysis):
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

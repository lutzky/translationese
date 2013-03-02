"""\
Punctuation marks organize the information within sentence boundaries and to a
great extent reduce ambiguity; according to the explicitation hypothesis,
translated texts are less ambiguous, and we assume that this tendency will
manifest itself in the (different) way in which translated texts are
punctuated.
"""
import translationese

punctuation_marks = [ '?', '!', ':', ';', '-', '(', ')', '[', ']',
                      "'", '"', '/', ',', '.' ]
"""Relevant punctuation marks"""

VARIANTS = [0, 1, 2]
"""Possible variants:

0. The normalized frequency of each punctuation mark in the chunk.

1. A non-normalized notion of frequency: n/tokens, where n is the number of
occurrences of a punctuation mark; and tokens is the actual (rather than
normalized) numbers of tokens in the chunk.  This value is magnified by an
order of 4.

2. n/p, where p is the total number of punctuations in the chunk; and n as
above. This value is magnified by an order of 4.
"""

def count_punctuation_marks(analysis):
    """Count the amount of punctuation marks in the text of ``analysis``."""
    histogram = dict([ (x, 0) for x in punctuation_marks ])
    count = 0
    for char in analysis.fulltext:
        if char in punctuation_marks:
            histogram[char] += 1
            count += 1
    return count, histogram

def quantify_variant(analysis, variant):
    """Quantify punctuation marks."""
    if not variant in [0, 1, 2]:
        raise translationese.NoSuchVariant()

    assert isinstance(analysis, translationese.Analysis)

    count, histogram = count_punctuation_marks(analysis)

    divideby = [
                translationese.expected_chunk_size,
                # The following two are magnified by 4.0, as in the paper
                len(analysis.tokens()) / 4.0,
                float(count) / 4.0,
                ]

    for char in punctuation_marks:
        histogram[char] /= divideby[variant]

    return histogram

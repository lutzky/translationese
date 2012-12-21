"""\
Implementation of Punctuation hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.5 Miscellaneous, Punctuation
"""
import translationese

main_attributes = [ '?', '!', ':', ';', '-', '(', ')', '[', ']',
                    "'", '"', '/', ',', '.' ]

# Attributes are identical for all three variants.
variant_attributes = [ main_attributes ] * 3

def count_punctuation_marks(analysis):
    histogram = dict([ (x, 0) for x in main_attributes ])
    count = 0
    for char in analysis.fulltext:
        if char in main_attributes:
            histogram[char] += 1
            count += 1
    return count, histogram

def quantify_variant(analysis, variant):
    if not variant in [0, 1, 2]:
        raise translationese.NoSuchVariant()

    assert isinstance(analysis, translationese.Analysis)

    count, histogram = count_punctuation_marks(analysis)

    divideby = [
                2000.0,
                # The following two are magnified by 4.0, as in the paper
                len(analysis.tokens()) / 4.0,
                float(count) / 4.0,
                ]

    for char in main_attributes:
        histogram[char] /= divideby[variant]

    return histogram

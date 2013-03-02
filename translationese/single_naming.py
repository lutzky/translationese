"""\
The frequency of proper nouns consisting of a single token, not having an
additional proper noun as a neighbor. As a contemporary example, it is common
to find in German news (as of 2012) the single proper name Westerwelle, but in
translating German news into another language, the translator is likely to add
the first name of this person (Guido) and probably his role, too (minister of
foreign affairs).
"""

from translationese.utils import is_proper_noun

def quantify(analysis):
    """Quantify single naming."""
    edge_marker = [('', '')]
    pos_tags = edge_marker + analysis.pos_tags() + edge_marker
    num_tags = len(pos_tags) - 2 # Remove 2 edge markers

    count = 0
    for i in range(len(pos_tags)):
        if     is_proper_noun(pos_tags[i])   and \
           not is_proper_noun(pos_tags[i-1]) and \
           not is_proper_noun(pos_tags[i+1]):
            count += 1

    return { "single_naming": float(count) / num_tags }

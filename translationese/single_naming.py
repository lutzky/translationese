"""\
Implementation of Single Naming hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.2 Explicitation, Single Naming.
"""

from translationese.utils import is_proper_noun

def quantify(analysis):
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

"""\
Implementation of Explicit Naming hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.2 Explicitation, Explicit Naming.
"""

from translationese import is_proper_noun
from pronouns import PRONOUNS as PRONOUNS_LIST

def quantify(analysis):
    proper_nouns = sum(1 for x in analysis.pos_tags() if is_proper_noun(x))

    pronouns = sum(1 for x in analysis.tokens() if x in PRONOUNS_LIST)

    return { "explicit_naming": 3.0 * (float(pronouns) / proper_nouns) }

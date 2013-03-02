"""\
We hypothesize that one form of explicitation in translations is the use of a
personal pronoun as a clarification of a proper noun. We calculate the ratio of
personal pronouns to proper nouns, both singular and plural, magnified by an
order of 3. See also :mod:`translationese.pronouns`.
"""

from pronouns import PRONOUNS as PRONOUNS_LIST
from translationese.utils import is_proper_noun

def quantify(analysis):
    """Quantify explicit naming."""
    proper_nouns = sum(1 for x in analysis.pos_tags() if is_proper_noun(x))

    pronouns = sum(1 for x in analysis.tokens() if x in PRONOUNS_LIST)

    return { "explicit_naming": 3.0 * (float(pronouns) / proper_nouns) }

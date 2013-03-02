"""\
Writers have a relatively limited vocabulary from which to choose words to open
or close a sentence. We hypothesize that the choices subject to interference.
The value of this feature is the normalized frequency of tokens appearing in
the first, second, antepenultimate, penultimate and last positions in a
sentence. We exclude sentences shorter than five tokens.  Punctuation marks are
considered as tokens in this feature, and for this reason the three last
positions of a sentence are considered, while only the first two of them are
interesting for our purposes.
"""

import translationese
from translationese.utils import sparse_dict_increment

POSITION_NAMES = {
                  "first": 0,
                  "second": 1,
                  "antepenultimate":-4,
                  "penultimate":-3,
                  "last":-2  # -1 is the period
                  }
"""Names of the various positions of the sentence, final period excluded."""

def quantify(analysis):
    """Analyze positional token frequency."""
    assert isinstance(analysis, translationese.Analysis)

    result = {}

    for sentence in analysis.tokenized_sentences():
        if len(sentence) < 6:
            # Sentence has fewer than 5 tokens (and a period)
            continue
        for position_name, position in POSITION_NAMES.items():
            key = "%s %s" % (position_name, sentence[position])
            sparse_dict_increment(result, key)

    return result

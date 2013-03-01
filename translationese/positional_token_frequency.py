import translationese
from translationese.utils import sparse_dict_increment

POSITION_NAMES = {
                  "first": 0,
                  "second": 1,
                  "antepenultimate":-4,
                  "penultimate":-3,
                  "last":-2  # -1 is the period
                  }
def quantify(analysis):
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


import translationese
from translationese import word_ranks

VARIANTS = [0, 1, 2] #: Possible variants

def quantify_variant(analysis, variant):
    assert isinstance(analysis, translationese.Analysis)

    num_top_words = [5, 10, 50]
    d = {}

    for word in word_ranks.TOP_WORDS[:num_top_words[variant]]:
        d[word] = 0

    for token in analysis.tokens():
        if token in d:
            d[token] += 1

    return {k: float(v) / len(analysis.tokens()) for (k, v) in d.items()}

from translationese.utils import output_filter_ngram, sparse_dict_increment
from translationese.function_words import FUNCTION_WORDS
import nltk.util

def function_word_or_POS(token, tag):
    if token.lower() in FUNCTION_WORDS:
        return token.lower()
    else:
        return tag

def trigram_is_functional(trigram):
    for w in trigram:
        if not w.isalpha(): return False

    num_function_words = sum(1 for token in trigram if token in FUNCTION_WORDS)
    return num_function_words >= 2

def quantify(analysis):
    d = {}

    word_stream = (function_word_or_POS(token, tag) for (token, tag)
                   in analysis.pos_tags())
    num_tokens = float(len(analysis.pos_tags()))

    for trigram in nltk.util.itrigrams(word_stream):
        if trigram_is_functional(trigram):
            sparse_dict_increment(d, trigram)

    return {output_filter_ngram(k): (v / num_tokens) for (k, v) in d.items()}

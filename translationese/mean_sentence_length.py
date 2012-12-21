"""\
Implementation of Mean Sentence Length hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.1 Simplification, Mean Sentence Length
"""

import nltk

attributes = [ "mean_sentence_length" ]

def quantify(analysis):
    result = len(analysis.tokens()) / float(len(analysis.sentences()))
    return { "mean_sentence_length": result }

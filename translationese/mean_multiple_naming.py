"""\
Implementation of Mean multiple naming hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.2 Expplicitation, Mean multiple naming
"""
from nltk.tag import pos_tag

__author__ = "Gal Star"
__email__ = "gal.star3051@gmail.com"

import nltk

def is_proper_noun(pos):
    return (pos == "NNP")

def tokens_without_punctuations (analysis):
    return len([x for x in analysis.case_tokens() if x.isalpha()])

def quantify(analysis):
    count = 0
    pos_tags = nltk.pos_tag(analysis.case_tokens())
    
    for token in pos_tags:
        if (token[1] == "NNP"):
            count += 1
    
    return { "mean_multiple_naming": count / float(tokens_without_punctuations(analysis)) }

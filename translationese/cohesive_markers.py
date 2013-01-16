"""\
Implementation of Cohesive Markers hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.2 Explicitation, Cohesive Markers
"""

import nltk

COHESIVE_MARKERS = ["as for",
"as to",
"because",
"besides",
"but",
"consequently",
"despite",
"even if",
"even though",
"except",
"further",
"furthermore",
"hence",
"however",
"in addition",
"in conclusion",
"in other words",
"in spite",
"instead",
"is to say",
"maybe",
"moreover",
"nevertheless",
"on account of",
"on the contrary",
"on the other hand",
"otherwise",
"referring to",
"since",
"so",
"the former",
"the latter",
"therefore",
"this implies",
"though",
"thus",
"with reference to",
"with regard to",
"yet",
"concerning"]

def quantify(analysis):
    result = {}
    for marker in COHESIVE_MARKERS:
        result[marker] = result.get(marker, 0)
    
    tokenized_markers = [(marker,nltk.word_tokenize(marker)) for marker in COHESIVE_MARKERS]
    text = analysis.tokens()
    
    for (i,word) in enumerate(text):
        for (marker,tokenized) in tokenized_markers:
            if (tokenized == text[i:i+len(tokenized)]):
                result[marker] = result.get(marker, 0) + 1

    pairs = [ (marker, float(result[marker]) / len(text)) for marker in COHESIVE_MARKERS]
    
    return dict(pairs)

attributes = COHESIVE_MARKERS
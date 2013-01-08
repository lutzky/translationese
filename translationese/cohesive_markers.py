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
    for mrk in COHESIVE_MARKERS:
        result[mrk] = result.get(mrk, 0)
    
    tokenized_markers = [(mrk,nltk.word_tokenize(mrk)) for mrk in COHESIVE_MARKERS]
    text = analysis.tokens()
    
    for (i,word) in enumerate(text):
        for (mrk1,mrk2) in tokenized_markers:
            if (mrk2 == text[i:i+len(mrk2)]):
                result[mrk1] = result.get(mrk1, 0) + 1

    pairs = [ (mrk, float(result[mrk]) / len(text)) for mrk in COHESIVE_MARKERS]
    return dict(pairs)

attributes = COHESIVE_MARKERS
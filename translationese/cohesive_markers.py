"""\
Implementation of Cohesive Markers hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.2 Explicitation, Cohesive Markers
"""

import nltk

COHESIVE_MARKERS = ["as for",
"as to",
"because",
"despite",
"even if"]

def quantify(analysis):
    histogram = analysis.histogram_normalized()
    bigram = analysis.bigrams()
    pairs = []
    
    for word in analysis.tokens():
        
    
    
    
    
    for marker in COHESIVE_MARKERS:
        tokenized_marker = nltk.word_tokenize(marker)
        marker_len = len(tokenized_marker)
        
        if (marker_len == 1):
            pairs += {(marker, histogram.get(marker, 0.0))}
            
        elif (marker_len == 2):
            new_marker = (tokenized_marker[0], tokenized_marker[1])
            pairs += {(marker, bigram.get(new_marker, 0.0))}
            
    print pairs
    return dict(pairs)

attributes = COHESIVE_MARKERS
"""\
Implementation of Punctuation hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.5 Miscellaneous, Punctuation
"""

attributes = [ '?', '!', ':', ';', '-', '(', ')', '[', ']', 
               "'", '"', '/', ',', '.' ]

def quantify(analysis):
    histogram = dict([ (x,0) for x in attributes ])
    for char in analysis.fulltext:
        if char in attributes:
            histogram[char] += 1

    # TODO: Implement normalization variants

    for char in attributes:
        histogram[char] /= 2000.0

    return histogram
        

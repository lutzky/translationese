"""\
Implementation of Pronouns hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.5 Miscellaneous, Pronouns
"""

PRONOUNS = [ 
 "he",
 "her",
 "hers",
 "herself",
 "him",
 "himself",
 "i",
 "it",
 "itself",
 "me",
 "mine",
 "myself",
 "one",
 "oneself",
 "ours",
 "ourselves",
 "she",
 "theirs",
 "them",
 "themselves",
 "they",
 "us",
 "we",
 "you",
 "yourself",
]

def quantify(analysis):
    freq = analysis.histogram_normalized()
    pairs = [ (word, freq.get(word, 0.0)) for word in PRONOUNS ]
    return dict(pairs)

attributes = PRONOUNS

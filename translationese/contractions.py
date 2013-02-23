"""\
Implementation of Lexical Variety hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.3 Normalization, Contractions
"""

import nltk

CONTRACTIONS = {
 "i'm": ["i am"],
 "it's": ["it is", "it has"],
 "there's": [ "there is", "there has" ],
 "he's": [ "he is", "he has" ],
 "she's": [ "she is", "she has" ],
 "what's": [ "what is", "what has" ],
 "let's": [ "let us" ],
 "who's": [ "who is", "who has" ],
 "where's": [ "where is", "where has" ],
 "how's": [ "how is", "how has" ],
 "here's": [ "here is" ],
 "i'll": [ "i will" ],
 "you'll": [ "you will" ],
 "she'll": [ "she will" ],
 "he'll": [ "he will" ],
 "we'll": [ "we will" ],
 "they'll": [ "they will" ],
 "i'd": [ "i would", "i had" ],
 "you'd": [ "you would", "you had" ],
 "she'd": [ "she would", "she had" ],
 "he'd": [ "he would", "he had" ],
 "we'd": [ "we would", "we had" ],
 "they'd": [ "they would", "they had" ],
 "i've": [ "i have" ],
 "you've": [ "you have" ],
 "we've": [ "we have" ],
 "they've": [ "they have" ],
 "who've": [ "who have" ],
 "would've": [ "would have" ],
 "should've": [ "should have" ],
 "must've": [ "must have" ],
 "you're": [ "you are" ],
 "they're": [ "they are" ],
 "we're": [ "we are" ],
 "who're": [ "who are" ],
 "couldn't": [ "could not" ],
 "can't": [ "cannot" ],
 "wouldn't": [ "would not" ],
 "don't": [ "do not" ],
 "doesn't": [ "does not" ],
 "didn't": [ "did not" ],
}

def quantify(analysis):
    histogram = analysis.bigrams()

    def contraction_ratio(contraction):
        tokenized = tuple(nltk.word_tokenize(contraction))
        contracted_count = histogram.get(tokenized, 0)

        if contracted_count == 0: return 0

        contracted_forms = [ tuple(x.split(" "))
                             for x in CONTRACTIONS[contraction] ]
        uncontracted_count = sum([ histogram.get(x, 0)
                                   for x in contracted_forms ])

        if uncontracted_count == 0:
            uncontracted_count = 1.0

        return contracted_count / float(uncontracted_count)

    pairs = [ (x, contraction_ratio(x)) for x in CONTRACTIONS.keys() ]
    return dict(pairs)

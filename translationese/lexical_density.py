"""\
Implementation of Lexical Density hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.1 Simplification, Lexical Density
"""

__author__ = "Gal Star"
__email__ = "gal.star3051@gmail.com"

attributes = [ "lexical_density" ]

def quantify(analysis):
    is_not_verb = lambda letter: letter !='V'
    is_not_noun = lambda letter: letter !='N'
    is_not_adjective = lambda letter: letter !='J'
    is_not_adverb = lambda letter: letter !='R'
        
    is_lexical_density = lambda l: is_not_verb(l) and is_not_noun(l) and \
            is_not_adjective(l) and is_not_adverb(l)
        
    return dict(loat(len([x for (x,y) in analysis.pos_tags() if is_lexical_density(y[0])])) / len(analysis.tokens()))


"""\
Implementation of Lexical Density hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.1 Simplification, Lexical Density
"""

__author__ = "Gal Star"
__email__ = "gal.star3051@gmail.com"

def quantify(analysis):
    all_tags = analysis.tokens()
    
    def is_lexical_density(letter):    
        is_not_verb = letter[0] !='V'
        is_not_noun = letter[0] !='N'
        is_not_adjective = letter[0] !='J'
        is_not_adverb = letter[0] !='R'
        
        return is_not_verb and is_not_noun and is_not_adverb and \
               is_not_adjective
    
    def count_all_lexical_pos_tags():
        text = analysis.pos_tags()
        return len([t for t in text if is_lexical_density(t[1])])
    
    result = float(count_all_lexical_pos_tags()) / len(all_tags)
    return { "lexical_density": result }

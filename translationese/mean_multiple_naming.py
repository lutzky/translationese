"""\
Implementation of Mean multiple naming hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.2 Expplicitation, Mean multiple naming
"""

import nltk
from translationese.utils import is_proper_noun

def quantify(analysis):
    num_proper_noun_runs = 0
    num_proper_noun_tokens = 0
    currently_in_run = False

    pos_tags = nltk.pos_tag(analysis.case_tokens())

    for token in pos_tags:
        if is_proper_noun(token):
            currently_in_run = True
            num_proper_noun_tokens += 1
        elif currently_in_run:
            # Run just ended
            currently_in_run = False
            num_proper_noun_runs += 1

    if num_proper_noun_runs == 0:
        result = 0
    else:
        result = float(num_proper_noun_tokens) / num_proper_noun_runs
    
    return { "mean_multiple_naming": result }

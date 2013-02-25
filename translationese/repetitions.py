import nltk
from collections import Counter

ignored_tokens = set([
    # Inflections of 'be'
    "am", "is", "are", "was", "were", "be", "being", "been", 
    # Inflections of 'have'
    "have", "has", "had", 
])

def proper_pos(token, pos):
    if token.lower() in ignored_tokens: return False

    if pos.startswith("NN"): return True # Noun
    if pos.startswith("VB"): return True # Verb
    if pos.startswith("JJ"): return True # Adjective
    if pos.startswith("RB"): return True # Adverb

    return False

def quantify(analysis):
    pos_tags = analysis.pos_tags()

    appropriate_tokens = (token.lower() for token, tag in pos_tags \
                          if proper_pos(token, tag))

    counter = Counter(appropriate_tokens)

    result = sum(occurrences for token, occurrences in counter.items()
                 if occurrences > 1)

    result *= 3.0
    result /= len(pos_tags)

    return { "repetitions": result }

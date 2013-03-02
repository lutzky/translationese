import translationese
import re

def syllables(word):
    """Approximate the number of syllables in ``word`` by counting
    vowel-sequences surrounded by consonants or space. Sometimes this works
    well:
    
    >>> syllables("the")
    1
    >>> syllables("augmented")
    3
    >>> syllables("may-day")
    2
    
    Sometimes it doesn't:
    
    >>> syllables("make")
    2
    >>> syllables("awesome")
    4
    >>> syllables("syllables")
    2
    
    For non-words, 0 is returned:
    
    >>> syllables(".")
    0
    """

    if not re.match('[a-z\-]', word):
        return 0

    split_by_consonant_sequences = re.split('[^aeiou]', word)
    empty_strings_removed = filter(None, split_by_consonant_sequences)

    return len(empty_strings_removed)

def quantify(a):
    assert isinstance(a, translationese.Analysis)

    num_syllables = sum(syllables(tok) for tok in a.tokens())

    return { 'syllable_ratio': float(num_syllables) / len(a.tokens()) }

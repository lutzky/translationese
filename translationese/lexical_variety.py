"""\
Implementation of Lexical Variety hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.1 Simplification, Lexical Variety
"""
import math

__author__ = "Ohad Lutzky"
__email__ = "ohad@lutzky.net"


attributes = [
    "type_token_ratio",
    "log_type_token_ratio",
    "unique_type_token_ratio",
]

class LexicalVarietyQuantifier:
    def unique_tokens(self):
        """Returns tokens occurring only once in the text."""
        return [ k for k, v in self.analysis.histogram().items() \
                if v == 1 ]

    def __init__(self, analysis):
        self.analysis = analysis
        self.num_tokens = len(analysis.tokens())
        self.num_types = len(analysis.tokens_set())
        self.num_unique_tokens = len(self.unique_tokens())

    def type_token_ratio(self):
        """Returns 6 times the type token ratio (as defined in the
        article)"""
        return 6 * (float(self.num_types) / self.num_tokens)

    def log_type_token_ratio(self):
        """Returns 6 times the lograithmic type token ratio (as defined
        in the article)"""
        return 6 * math.log(self.num_types) / math.log(self.num_tokens)

    def unique_type_token_ratio(self):
        return 100 * math.log(self.num_tokens) / \
            (1 - (self.num_unique_tokens / float(self.num_types)))

def quantify(analysis):
    quantifier = LexicalVarietyQuantifier(analysis)
    return dict([ (k, getattr(quantifier, k)()) for k in attributes ])
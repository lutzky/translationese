attributes = ["type_token_ratio"]

# TODO: Logarithmic, V1 (see article)

def quantify(analysis):
    num_types = len(analysis.tokens_set())
    num_tokens = len(analysis.tokens())
    ratio = float(num_types) / num_tokens
    return { "type_token_ratio": ratio }

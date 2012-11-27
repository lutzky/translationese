import nltk

def get_words(s):
    # We tokenize into sentences and then into words due to a warning
    # in the NLTK API doc to only word_tokenize single sentences.

    sentences = nltk.sent_tokenize(s)

    words = []

    for sentence in sentences:
        words += nltk.word_tokenize(sentence)

    return words

def average_sentence_length(s):
    sentence_length = lambda sentence: len(nltk.word_tokenize(sentence))

    sentences = nltk.sent_tokenize(s)

    return float(sum([sentence_length(x) for x in sentences])) / len(sentences)

def mean_word_length(s):
    sentences = nltk.sent_tokenize(s)
    words = []
    for sentence in sentences: words += nltk.word_tokenize(sentence)

    real_words = [w for w in words if w[0].isalpha()]
    return float(sum([len(w) for w in real_words])) / len(real_words)

def type_token_ratio(s):
    words = [ w.upper() for w in get_words(s) ]
    
    return len(set(words)) / float(len(words))

def most_frequent_words(s, n):
    words = [ w.upper() for w in get_words(s) ]

    words_set = set(words)

    words_freqs = [ (w, words.count(w)) for w in words_set ]

    words_freqs.sort(key = lambda x: x[1], reverse = True)

    return [ x[1] / float(len(words)) for x in words_freqs[0:n]]
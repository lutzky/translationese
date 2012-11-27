import nltk

def average_sentence_length(s):
    sentence_length = lambda sentence: len(nltk.word_tokenize(sentence))

    sentences = nltk.sent_tokenize(s)

    return float(sum([sentence_length(x) for x in sentences])) / len(sentences)

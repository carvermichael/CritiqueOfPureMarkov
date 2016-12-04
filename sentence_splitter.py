from nltk import tokenize


def get_sentences(file_name):
    with open(file_name, 'r') as file:
        return tokenize.sent_tokenize(file.read().replace('\n', ' '))

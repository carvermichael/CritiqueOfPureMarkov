import chain_creator
import random


def create_status(number_leading_words):
    chain = chain_creator.get_chain('CPR.txt')
    current_key = []

    for i in range(number_leading_words):  # number_leading_words implicated here
        current_key.append('__BEGIN__')

    current_key = tuple(current_key)
    beginning_key = current_key

    return_sentence = ''

    while len(return_sentence) <= 20 or len(return_sentence) >= 140:
        sentence = []
        current_key = beginning_key
        while True:
            next_word = get_next_word(current_key, chain)
            if next_word == '__END__':
                break
            else:
                sentence.append(next_word)
                current_key = (current_key[1], current_key[2], next_word)  # number_leading_words implicated here
        return_sentence = ' '.join(sentence)

    return return_sentence


def get_next_word(current_key, chain):
    inner_dict = chain.get(current_key)
    choice_list = []

    for key in inner_dict.keys():
        for i in range(inner_dict.get(key)):
            choice_list.append(key)

    return random.choice(choice_list)


def main():
    blah = create_status(3)
    print(blah)
    print('len:', len(blah))

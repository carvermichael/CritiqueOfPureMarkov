import sentence_splitter
import unittest

BEGIN = '__BEGIN__'
END = '__END__'
number_leading_words = 3


def make_chain(file_name):
    chain = {}

    sentences = sentence_splitter.get_sentences(file_name)
    for sentence in sentences:
        sentence = ' '.join(sentence.split())
        # create list, start with # of BEGINs
        words = []
        for i in range(number_leading_words):  # number_leading_words implicated here
            words.append(BEGIN)

        # split into individual words, appends to BEGINs
        words = words + sentence.split(' ')

        # set last word in sentence to END
        words.append(END)

        # flip through words in sentence --> create chain
        while len(words) > 3:  # number_leading_words implicated here
            outer_key = (words[0], words[1], words[2])  # number_leading_words implicated here
            inner_key = words[3]  # number_leading_words implicated here
            if outer_key in chain:
                inner_dict = chain.get(outer_key)
                if inner_key in inner_dict:
                    inner_dict[inner_key] = inner_dict.get(inner_key) + 1
                else:
                    inner_dict[inner_key] = 1
            else:
                chain[outer_key] = {inner_key: 1}

            words.pop(0)

    return chain


class ChainCreatorTests(unittest.TestCase):
    def test_chain(self):
        # sample_text = 'This is just. This is not. What is this?'
        expected_chain = {
            (BEGIN, BEGIN): {'This': 2, 'What': 1},
            (BEGIN, 'This'): {'is': 2},
            (BEGIN, 'What'): {'is': 1},
            ('This', 'is'): {'just.': 1, 'not.': 1},
            ('What', 'is'): {'this?': 1},
            ('is', 'just.'): {END: 1},
            ('is', 'not.'): {END: 1},
            ('is', 'this?'): {END: 1}
        }

        # this doesn't work
        # not sure how to compare dicts yet
        self.assertEqual(make_chain('sample_text.txt'), expected_chain)


if __name__ == '__main__':
    unittest.main()

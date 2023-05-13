import parser

text = input('Enter the text:\n')

print('Enter K and N value to search top-K repeated N-grams it the text.')
while True:
    k = input('Enter K: ')
    if k.isdigit():
        k = int(k)
        break
    else:
        print('Error. Enter an integer value.')
while True:
    n = input('Enter N: ')
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Error. Enter an integer value.')

sentences = parser.sentences_split(text)
sentences_amount = parser.sentences_amount(sentences)
non_declarative_sentences_amount = parser.non_declarative_sentences_amount(sentences)
average_sentences_length = parser.average_sentence_length(sentences)
average_word_length = parser.average_word_length(text)
n_grams = parser.top_n_grams(k, n, sentences)

print('Amount of sentences: ', sentences_amount)
print('Amount of non-declarative sentences: ', non_declarative_sentences_amount)
print('Average length of the sentence in characters: ', average_sentences_length)
print('Average length of the word in the text in characters', average_word_length)

if n_grams == {}:
    print('No {0}-grams found.'.format(n))
else:
    print('List of top-{0}, {1}-grams: '.format(k, n))
    for gram, count in n_grams.items():
        print('Count: {0:>3} | {1}-gram: {2}'.format(count, n, ' '.join(gram)))
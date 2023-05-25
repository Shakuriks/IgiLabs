import parser1

def test_sentences_split_1():
    res = parser1.sentences_split('Hello! World?')
    assert len(res) == 2
    assert res == ['Hello!', 'World?']


def test_sentences_split_2():
    res = parser1.sentences_split('Smth?.. "Smth, smth, smth!" Smth...')
    assert len(res) == 3
    assert res == ['Smth?..', '"Smth, smth, smth!"', 'Smth...']


def test_sentences_split_3():
    res = parser1.sentences_split('N. V. Legonkov. Dr. Watson! Mr. Nobody, \'smth!..\'')
    assert len(res) == 3
    assert res == ['N. V. Legonkov.', 'Dr. Watson!', 'Mr. Nobody, \'smth!..\'']

def test_sentences_amount_1():
    sent = parser1.sentences_split('Mr.Smb! How are you?.. I\'m fine!')
    res = parser1.sentences_amount(sent)
    assert res == 3


def test_non_declarative_sentences_amount_1():
    sent = parser1.sentences_split('Smth!.. Smth... Smth. Smth?.. Smth! Smth smth smth. "Test..."')
    res = parser1.non_declarative_sentences_amount(sent)
    assert res == 4


def test_average_sentence_length_1():
    sent = parser1.sentences_split('Smth!.. Smth... Smth Smth?.. Smth smth smth.')
    res = parser1.average_sentence_length(sent)
    assert res == 7


def test_average_word_length_1():
    res = parser1.average_word_length('Smth smth. testing')
    assert res == 5


def test_top_n_grams_1():
    sent = parser1.sentences_split('Smth not. Smth not smth not smth one two one not one two. Two one two!..')
    res = parser1.top_n_grams(5, 2, sent)
    assert res == {"('smth', 'not')": 3, "('one', 'two')": 3, "('not', 'smth')": 2, "('two', 'one')": 2, "('smth', 'one')": 1}

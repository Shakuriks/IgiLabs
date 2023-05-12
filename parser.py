import re


def sentences_split(text):
    abbreviations = ['mr', 'mrs', 'ms', 'dr', 'prof', 'rev', 'etc', 'vs.', 'pl.', 'jr.']
    sentence_pattern = r'^.*?[.?!](?= |\w|$|"|\')'
    sentences = []

    match = re.search(sentence_pattern, text)
    while match:
        sentence = match.group()

        sentences.append(sentence)
        text = re.sub(re.sub(r'\?', '\\' + '?', sentence), '', text, count=1)

        single_quotes_count = len(re.findall(r'\'', sentences[-1]))
        double_quotes_count = len(re.findall(r'\"', sentences[-1]))
        open_bracket_count = len(re.findall(r'\(', sentences[-1]))
        closing_bracket_count = len(re.findall(r'\)', sentences[-1]))

        for word in text:
            if word == ' ':
                text = text[1:]
                continue
            if word == '\'':
                if single_quotes_count & 1 == 0:
                    break
                else:
                    sentences[-1] = sentences[-1] + '\''
                    text = text[1:]
                    continue
            if word == '\"':
                if double_quotes_count & 1 == 0:
                    break
                else:
                    sentences[-1] = sentences[-1] + '\"'
                    text = text[1:]
                    continue
            if word == ')':
                if open_bracket_count - closing_bracket_count == 0:
                    break
                else:
                    sentences[-1] = sentences[-1] + ')'
                    closing_bracket_count = closing_bracket_count + 1
                    text = text[1:]
                    continue
            break

        match = re.search(sentence_pattern, text)

    i = 0

    while i < len(sentences) - 1:
        for abbreviation in abbreviations:
            if re.search(r'\b' + abbreviation + r'\. *$', sentences[i],
                         re.IGNORECASE):  # and sentences[i + 1][0].isalpha()
                sentences[i] = sentences[i] + ' ' + sentences[i + 1]
                del sentences[i + 1]
                i = i - 1
                break
        i = i + 1

    i = 0

    while i < len(sentences) - 1:
        if (len(sentences[i]) > 2 and sentences[i][-3].isalpha() == False and sentences[i][-2].isalpha() and
            sentences[i][-1] == '.') \
                or (len(sentences[i]) <= 2 and sentences[i][-2].isalpha() and sentences[i][-1] == '.') \
                or (sentences[i][:-1].isdigit() and sentences[i][-1] == '.'):
            sentences[i] = sentences[i] + ' ' + sentences[i + 1]
            del sentences[i + 1]
            continue
        i = i + 1

    return sentences


def sentences_amount(sentences):
    return len(sentences)


def non_declarative_sentences_amount(sentences):
    count = 0
    for sentence in sentences:
        if (sentence[-1] == '.' and sentence[-2] != '.') \
                or (len(sentence) > 3 and (sentence[-1] == '"' or sentence[-1] == '\'')
                    and sentence[-2] == '.' and sentence[-3] != '.') \
                or (len(sentence) > 3 and sentence[-1] == '.' and sentence[-2] == '.'
                    and sentence[-3] == '.') \
                or (len(sentence) > 4 and (sentence[-1] == '"' or sentence[-1] == '\'')
                    and sentence[-2] == '.' and sentence[-3] == '.' and sentence[-4] == '.'):
            count = count + 1
    return count


def word_list(text):
    word_pattern = r'\b(?!\d+\b)[\w\']+\b'
    words = re.findall(word_pattern, text)
    return words


def average_word_length(text):
    words = word_list(text)
    average_length = sum(map(len, words)) / len(words)
    return average_length
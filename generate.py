from collections import defaultdict
import string

def whitespace_word_tokenize(sentence):
    chunks = sentence.split(' ')
    return [c.strip(string.punctuation) for c in chunks]


def process_sentence_list(sentence_list):
    sentence_stats, sentence_wordcounts = zip(*map(process_sentence, sentence_list))



def process_sentence(sentence):
    wordcount = defaultdict(int)
    stats = defaultdict(float)
    words = whitespace_word_tokenize(sentence)
    word_stats = map(process_word, words)

    totals_dict = defaultdict(list)

    for d in word_stats:
        for k, v in d.items():
            totals_dict[k].append(v)

    for k, v in totals_dict.items():
        stats[k] = sum(v)

    for w in words:
        wordcount[w.upper()] += 1

    # Character-based sentence stats
    for c in sentence:
        if c in string.punctuation:
            stats['t!@#'] += 1
            stats[c] += 1

    # Special stats:
    stats['avg_word_len'] = stats['tc'] / len(words)

    return stats, wordcount

def process_word(word):
    stats = defaultdict(float)
    stats['tc'] += len(word)

    for c in word:
        stats['tABC'] += c.isupper()
        stats['t123'] += c.isdigit()

        if c.isalpha():
            stats['tabc'] += 1
            stats[c.upper()] += 1


    stats['words'] = 1
    stats['short_words'] = 1 if len(stats) < 0 else 0

    return stats



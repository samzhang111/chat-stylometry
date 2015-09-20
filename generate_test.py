from __future__ import print_function
from pyspecs import *
import sys
import generate

# TODO: add statistical features
with when.supplied_a_list_of_sentences:
    sentence_list = ["This... is",
                     "2 sample sentence!"]

    fixtures = {
            'tc': 21,
            'tabc': 20,
            'tABC': 1,
            't123': 1,
            't!@#': 4,
            'T': 2,
            'H': 1,
            'I': 2,
            'S': 4,
            'A': 1,
            'M': 1,
            'P': 1,
            'L': 1,
            'E': 4,
            'N': 2,
            'C': 1,
            '.': 3,
            '!': 1,
            'avg_word_len': 21.0/5,
            }

    with then.stats_are_generated_from_the_list_of_sentences:
        stats = generate.process_sentence_list(sentence_list)
        for key, expectation in fixtures.iteritems():
            the((key, stats[key])).should.equal((key, expectation))


with when.supplied_a_sentence:
    sentence = "This... is sample sentence!"
    fixtures = {
            'tc': 20,
            'tabc': 20,
            'tABC': 1,
            't123': 0,
            't!@#': 4,
            'T': 2,
            'H': 1,
            'I': 2,
            'S': 4,
            'A': 1,
            'M': 1,
            'P': 1,
            'L': 1,
            'E': 4,
            'N': 2,
            'C': 1,
            '.': 3,
            '!': 1,
            'avg_word_len': 5,
            }
    bag_of_words_fixtures = {
            'THIS': 1,
            'IS': 1,
            'SAMPLE': 1,
            'SENTENCE': 1
            }
    with then.stats_are_generated_from_the_sentence:
        stats, wordcount = generate.process_sentence(sentence)
        for key, expectation in fixtures.iteritems():
            the((key, stats[key])).should.equal((key, expectation))

        for key, expectation in bag_of_words_fixtures.iteritems():
            the((key, wordcount[key])).should.equal((key, expectation))

with when.supplied_a_word:
    word = "Hello"
    with then.stats_are_generated_from_the_word:
        stats = generate.process_word(word)

        the(stats['tc']).should.equal(5)
        the(stats['tabc']).should.equal(5)
        the(stats['tABC']).should.equal(1)
        the(stats['t123']).should.equal(0)
        the(stats['t!@#']).should.equal(0)


        the(stats['H']).should.equal(1)
        the(stats['E']).should.equal(1)
        the(stats['L']).should.equal(2)
        the(stats['O']).should.equal(1)
        the(stats['!']).should.equal(0)

        the(stats['words']).should.equal(1)
        the(stats['short_words']).should.equal(0)


#with given.text_in_paragraph_form:
#    text = [map(tokenize, ["This is sentence 1 of paragraph 1.", "This is sentence 2 of paragraph 1."]),
#            map(tokenize, ["This is sentence 1 of paragraph 2.", "This is sentence 2 of paragraph 2."])]


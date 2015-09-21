from __future__ import print_function
from pyspecs import *
import sys
import generate

def visit(nested_dict):
    for k, v in nested_dict.iteritems():
        if isinstance(v, dict):
            for k, v2 in visit(v):
                pass
        else:
            yield k, v

#with when.supplied_a_list_of_sentences:
#    sentence_list = ["This... is",
#                     "2 sample sentence!"]
#
#    fixtures = {
#            'tc': 21,
#            'tabc': 20,
#            'tABC': 1,
#            't123': 1,
#            't!@#': 4,
#            'chars': {
#                'T': 2,
#                'H': 1,
#                'I': 2,
#                'S': 4,
#                'A': 1,
#                'M': 1,
#                'P': 1,
#                'L': 1,
#                'E': 4,
#                'N': 2,
#                'C': 1,
#                '.': 3,
#                '!': 1,
#                },
#            'avg_word_len': 21.0/5,
#            }
#
#    with then.stats_are_generated_from_the_list_of_sentences:
#        stats = generate.process_sentence_list(sentence_list)
#        for key, expectation in visit(fixtures):
#            the((key, stats[key])).should.equal((key, expectation))


#with given.a_sentence:
#    with when.stats_are_calculated_for_the_sentence:
#        sentence = "This... is sample sentence!"
#        fixtures = {
#                'summable': {
#                    'tc': 20,
#                    'tabc': 20,
#                    'tABC': 1,
#                    't123': 0,
#                    't!@#': 4,
#                    },
#                'chars': {
#                    'T': 2,
#                    'H': 1,
#                    'I': 2,
#                    'S': 4,
#                    'A': 1,
#                    'M': 1,
#                    'P': 1,
#                    'L': 1,
#                    'E': 4,
#                    'N': 2,
#                    'C': 1,
#                    '.': 3,
#                    '!': 1,
#                    },
#                'calculated': {
#                    'avg_word_len': 5,
#                    }
#                }
#        bag_of_words_fixtures = {
#                'THIS': 1,
#                'IS': 1,
#                'SAMPLE': 1,
#                'SENTENCE': 1
#                }
#        stats, wordcount = generate.process_sentence(sentence)
#        with then.a_nested_stats_structure_is_created:
#            the(dict(stats)).should.equal(dict(fixtures))
#
#        with then.stats_are_generated_from_the_sentence:
#            for key, expectation in visit(fixtures):
#                the((key, stats[key])).should.equal((key, expectation))
#
#            for key, expectation in bag_of_words_fixtures.iteritems():
#                the((key, wordcount[key])).should.equal((key, expectation))

with given.a_word:
    word = "Hello"

    with when.stats_are_calculated_for_a_word:
        stats = generate.process_word(word)
        fixtures = {
                'summable': {
                    'tc':5,
                    'tabc':5,
                    'tABC':1,
                    't123':0,
                    't!@#':0,
                    'short_words':0,
                    },
                'chars': {
                    'H':1,
                    'E':1,
                    'L':2,
                    'O':1,
                    '!':0,
                    },

                }

        with then.a_nested_stats_structure_is_created:
            the(dict(stats)).should.equal(dict(fixtures))
        with then.stats_are_generated_from_the_word:
            for key, expectation in visit(fixtures):
                the((key, stats[key])).should.equal((key, expectation))


#with given.text_in_paragraph_form:
#    text = [map(tokenize, ["This is sentence 1 of paragraph 1.", "This is sentence 2 of paragraph 1."]),
#            map(tokenize, ["This is sentence 1 of paragraph 2.", "This is sentence 2 of paragraph 2."])]


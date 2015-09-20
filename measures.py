'''
Statistical measures of authorship
'''
from __future__ import print_function
from collections import defaultdict
import sys


def hapax_legomena(wordcounts):
    unique_words = 0.0
    total_words = 0.0
    for counts in wordcounts.itervalues():
        unique_words += (counts == 1)
        total_words += counts

    return unique_words / total_words


def hapax_dislegomena(wordcounts):
    twice_seen_words = 0.0
    total_words = 0.0
    for counts in wordcounts.itervalues():
        twice_seen_words += (counts == 2)
        total_words += counts

    return twice_seen_words / total_words


def yules_i(wordcounts):
    m1 = 0.0
    m2 = 0.0

    for counts in wordcounts.itervalues():
        m1 += counts
        m2 += counts ** 2

    return (m1 * m1) / (m2 - m1)


def calculate_v(wordcounts):
    '''
    V(i, N) is the frequency of tokens appearing i times in a corpus of N total words.

    '''

    freqs_seen = defaultdict(float)
    total = 0.0
    for counts in wordcounts.itervalues():
        freqs_seen[counts] += 1
        total += counts

    V = {}
    for count, seen in freqs_seen.iteritems():
        V[count] = seen / total

    return V


def simpsons_d(wordcounts, V):
    simpsons_d = 0.0
    total = float(sum(wordcounts.itervalues()))

    for counts in wordcounts.itervalues():
        simpsons_d += V[counts] * (counts / total) * ((counts - 1) /
                                                      (total - 1))

    return simpsons_d


def sichels_s(wordcounts):
    return hapax_dislegomena(wordcounts) / \
           len(wordcounts)

def brunets_w(wordcounts):
    vocab_size = len(wordcounts)
    corpus_size = sum(wordcounts.values())

    return corpus_size ** (vocab_size ** -0.172)


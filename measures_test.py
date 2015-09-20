from __future__ import print_function
from pyspecs import *
import measures
import sys

with given.wordcounts_for_a_document:
    wordcounts = {"the": 5, "horse": 2, "ran": 1}


    with when.calculating_hapax_legomena:
        hapax_legomena = measures.hapax_legomena(wordcounts)

        with then.it_should_return_the_frequency_of_once_occurring_words:
            the(hapax_legomena).should.equal(1.0 / 8)

    with when.calculating_hapax_dislegomena:
        hapax_dislegomena = measures.hapax_dislegomena(wordcounts)
        with then.it_should_return_the_frequency_of_twice_occurring_words:
            the(hapax_dislegomena).should.equal(1.0 / 8)

    with when.calculating_yules_i:
        yules_i = measures.yules_i(wordcounts)
        with then.it_should_return_yules_i:
            m1 = 8.0
            m2 = 5 ** 2 + 2 ** 2 + 1 ** 2
            answer = m1 * m1 / (m2 - m1)
            the(yules_i).should.equal(answer)

    with when.the_V_distribution_is_needed:
        V = measures.calculate_v(wordcounts)

        with then.it_should_calculate_the_V_distribution:
            the(V).should.equal({
                    1: 1.0/8,
                    2: 1.0/8,
                    5: 1.0/8
                })

    with when.calculating_simpsons_d:
        V = measures.calculate_v(wordcounts)
        simpsons_d = measures.simpsons_d(wordcounts, V)
        with then.it_should_return_simpsons_d:
            answer = V[5] * (5.0/8) * (4.0/7) + \
                     V[2] * (2.0/8) * (1.0/7) + \
                     V[1] * (1.0/8) * (0)

            the(simpsons_d).should.equal(answer)

    with when.calculating_sichels_s:
        sichels_s = measures.sichels_s(wordcounts)

        with then.it_should_equal_the_ratio_of_twice_occurring_words_to_the_vocab_size:
            the(sichels_s).should.equal(measures.hapax_dislegomena(wordcounts) /
                                        len(wordcounts))


    with when.calculating_brunets_w:
        brunets_w = measures.brunets_w(wordcounts)

        with then.it_should_equal_the_brunets_w:
            total = sum(wordcounts.values())
            exponent = len(wordcounts) ** -0.172

            the(brunets_w).should.equal(total ** exponent)



    with when.calculating_honores_r:
        V = measures.calculate_v(wordcounts)
        honores_r = measures.honores_r(wordcounts, V)

        with then.it_should_correctly_calculate_honores_r:
            from math import log
            answer = 100 * log(sum(wordcounts.values())) / (1 - V[1]/len(wordcounts))
            the(honores_r).should.equal(answer)


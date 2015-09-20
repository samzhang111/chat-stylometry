from pyspecs import *
import measures

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



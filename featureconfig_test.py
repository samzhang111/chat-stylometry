from pyspecs import *
from featureconfig import FeatureConfig

features = {
        'word': {
            'short_word': {
                'summable': True,
                'filter': lambda w: True,
                'action': lambda w: len(w) <= 4
                }
            },
        'char': {
            'tc': {
                'summable': True,
                'filter': lambda c: True,
                'action': lambda c: 1
                },
            'tabc': {
                'summable': True,
                'filter': lambda c: c.isalpha(),
                'action': lambda c: 1
                },
            'tABC': {
                'summable': True,
                'filter': lambda c: c.isupper(),
                'action': lambda c: 1
                },
            't123': {
                'summable': True,
                'filter': lambda c: c.isdigit(),
                'action': lambda c: 1
                },
            't!@#': {
                'summable': True,
                'filter': lambda c: c in string.punctuation,
                'action': lambda c: 1
                },
            'chars': {
                'summable': False,
                'filter': lambda c: True,
                'type': 'nested',
                'action': lambda d, c: d[c] + 1 if d else defaultdict(int)
                }
            }
        }

with given.a_FeatureConfig_initialized_with_a_dictionary:
    fc = FeatureConfig(features)
    with when.processing_a_word_feature:
        with then.it_runs_all_word_features:
            pass

import string
import numpy as np
from collections import defaultdict
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
import sys
from pprint import pprint

class ChatFeatureExtractor(object):
    def __init__(self):
        with open('function_words.txt') as f:
            self.function_words = set([x.strip() for x in f])

    def extract(self, text):
        """
        Extract features from informal text.

        Implementation of lexical and word-based features of Zheng et al. (2005) "A Framework
        for Authorship Identification of Online Messages: Writing-Style
        Features and Classification Techniques"

        text: string
        
        """
        features = defaultdict(int)
        total_len = len(text)
        

        #######################################
        #           XXX
        # We currently have all features laid out flat.
        # In other words, there is no way to account for 'distortion' unless
        # we keep track of the keys.
        #
        # Do we want this, or do we want a nested structure, where say the
        # letters were a dict all under a single key.
        #
        #######################################
        # Force features to have all punctuation
        for x in string.punctuation:
            features[x] = 0

        # Force features to have all lower-case letters
        for x in string.ascii_lowercase:
            features[x] = 0
        
        # Lexical features:
        for c in text:
            features['1_alphas'] += c.isalpha()
            features['uppers'] += c.isupper()
            features['digits'] += c.isdigit()
            features['whitespaces'] += c.isspace()
            features['tab_chars'] += c == '\t'
            
            if c.isalpha():
                features[c.lower()] += 1
            
            if c in string.punctuation:
                features[c] += 1
        
        # Word-based features:

        # First tokenize into sentences
        pst = PunktSentenceTokenizer()
        sentences = pst.sentences_from_text(text)
        
        # Set function words to be mandatory features
        for x in self.function_words:
            features[x] = 0

        swords = map(nltk.word_tokenize, sentences)
        words = []

        for x in sentences:
            words.append(nltk.word_tokenize(x))
        
        for w in words:
            features['total_words'] += 1
            features['words_4'] += len(w) > 4
            features['words_chars'] += len(w)

        
        # Add sentence-level and statistical features TODO

        return features

if __name__ == '__main__':
    cfe = ChatFeatureExtractor()

    f = cfe.extract(sys.stdin.read())
    pprint(dict(f))

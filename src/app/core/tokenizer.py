import logging

logger = logging.getLogger(__name__)

"""
Tokenizer class is responsible for breaking the sentence into words separated by space.
It takes the sentence as a string and then return the array of strings as words.
"""
class Tokenizer:

    def __init__(self, sentence):
        self._words = sentence.split(" ")

    def get_words(self): return self._words
        

    

# your code goes here!
from collections import Counter

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.counter = Counter(self.word)

    def match(self, words):
        return [word for word in words if Counter(word.lower()) == self.counter and word.lower() != self.word]



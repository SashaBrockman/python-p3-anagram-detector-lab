# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    @property
    def word(self):
        """The word property"""
        return self._word
    
    @word.setter
    def word(self, word):
        """The word setter property"""
        self._word = word 

    def match(self, words):
        letter_list = [letter for letter in self.word]
        matches = []
        for item in words:
            comp_word = [word_letter for word_letter in item]
            if sorted(letter_list) == sorted(comp_word):
                matches.append(item)
        
        return matches
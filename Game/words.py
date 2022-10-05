import random

class Words:
    """A list of possible words to be guessed to the player
    
    The responsability of Words is to display a word from a list of words and
    to keep track of the letters guessed for the player
    
    Attributes_
        word (list): List of possible words
        guessed_letters (list): A list of the guessed letters
    """

    def __init__(self):
        self._word = ["apple", "pineapple", "tomato", "apricot", "potato"
        , "avocado", "orange", "blueberry", "cranberry", "banana"]
        self._guessed_letters = []
    
    def get_word(self):
        return self._word

    def get_guessed_letters(self):
        return self._guessed_letters

    def hiden_word(self):
        secret_word = random.choise(self.get_word())
        return secret_word
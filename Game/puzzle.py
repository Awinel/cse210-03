from CSE 210.cse210-03.Game.words import Words


class Puzzle:
    """The hiden word that will be desplay when the player guesses correctly

    The responsabiliti of Puzzle is to keep the secret word
    
    Attributes:
        words (list(Words)): A list for a possible word to be guess
        hidden_word (int): The secret word
    """

    def __init__(self):
        self._words = Words()
        self._player_guess = ""
        self._word = self._words.hiden_word()
    
    def hidden_word(self):
        secret_word = []
        for letter in self._word:
            secret_word.append(letter)
        return secret_word
    
    
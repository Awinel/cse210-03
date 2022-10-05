



from CSE 210 .cse210-03.Game.words import Words


class Puzzle:
    """The hiden word that will be desplay when the player guesses correctly

    The responsabiliti of Puzzle is to keep the secret word and when the player
    guesses correctly display the correct letter
    
    Attributes:
        words (list(Words)): A list for a possible word to be guess
        is_playing (boolean): whether or not the game is being played
    """

    def __init__(self):
        self._words = Words()
        self._player_guess = ""
        self._word = self._words.hiden_word()
    
    def hidden_word(self):
        for _ in self._word:
            print("_", end="")
    
    def guess(self):
        letter_guessed = self._player_guess
        return letter_guessed

    def guessed(self):
        word = self._word
        for letter in word:
            if self.guess == letter:
                print(letter, end="")
            else:
                print("_", end="")

# from CSE 210.cse210-03.Game.parachute import Parachute
# from CSE 210.cse210-03.Game.puzzle import Puzzle

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
        secret_word = random.choice(self.get_word())
        return secret_word

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
        for letter in self._word:
            if letter in (self._right_letters):
                print("letter", end=" ")
            else:
                print("_", end=" ")
    
    def guess(self):
        self._player_guess = input("Guess a letter [a-z]: ")
        letter_guessed = self._player_guess
        return letter_guessed

class Parachute():
    """The picture of a parachute
    
    The responsability of Parachute is to display the whole image
    
    Attributes:
        picture (list): List that will contain each part of the parachute
    """

    def __init__(self):
        self._picture = []
    
    def whole_parachute(self):
        self._picture = [
         " ___",
        "/___\\",
        "\   /",
         " \ /",
          "  O",
         " /|\\",
         " / \\",
         "^^^^^^^^^"
        ]
        print(self._picture[0])
        print(self._picture[1])
        print(self._picture[2])
        print(self._picture[3])
        print(self._picture[4])
        print(self._picture[5])
        print(self._picture[6])
        print("")
        print(self._picture[7])

    def index_parachute(self):
        index = self._picture
        return index

class Director():
    """A person that directs the game
    
    The responsability of Director is to control the secuense of the play
    
    Attributes:
        is_playing (boolean):
        game_over:
        letters_right:
        puzzle:
        parachute:
        index:
        """
    def __init__(self):
        self._puzzle = Puzzle()
        self._parachute = Parachute()
        self._get_index = self._parachute.index_parachute()
        self._right_letters = []
        self._wrong_letters =[]

    def is_playing(self):
        while self.game_over != True:
            self._puzzle.hidden_word()
            print("")
            self._parachute.whole_parachute()
            self._puzzle.guess()
    
    def guessed(self):
        word = self._word
        user_guess = self.guess
        for letter in word:
            if user_guess == letter:
                self._right_letters.append(user_guess)
            else:
                self._wrong_letters.append(user_guess)

    def game_over(self):
        if self._get_index[4] == "  X":
            print("Game Over")
            return True
        else:
            return False

director = Director()
director.is_playing()

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

    The responsabiliti of Puzzle is to keep the secret word and ask the user for a letter
    
    Attributes:
        words (list(Words)): A list for a possible word to be guess
        hidden_word (int): The secret letter
        guess (input): The question for the user and then return the value
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

class Parachute():
    """The picture of a parachute
    
    The responsability of Parachute is to display the whole image
    
    Attributes:
        picture (list): List that will contain each part of the parachute
    """

    def __init__(self):
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
    
    def whole_parachute(self):
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
        self._secret_word = self._puzzle.hidden_word()
        self._right_letters = []
        self._wrong_letters =[]
        self._player_guess = ""
        self._win_check = []

    def is_playing(self):
        while self.game_over != True:
            secret_word = self._secret_word
            for letter in secret_word:
                if self._player_guess == letter and (self._player_guess not in self._right_letters):
                    self._right_letters.append(letter)
                    self._win_check.append(letter)
                else:
                    self._wrong_letters.append(self._player_guess)
            for i in secret_word:
                if i in self._right_letters:
                    print(i, end=" ")
                else:
                    print("_", end=" ")
            print("")
            self._parachute.whole_parachute()
            self._player_guess = input("Guess a letter [a-z]: ")
            print(self._right_letters)
            print(self._win_check)

    def game_over(self):
        if self._get_index[4] == "  X":
            print("Game Over")
            return True
        elif len(self._win_check) == len(self._right_letters):
            print("You Win")
            return False
        else:
            return False

director = Director()
director.is_playing()
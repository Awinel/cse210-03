
from Game.parachute import Parachute
from Game.puzzle import Puzzle

class Director():
    """A person that directs the game
    
    The responsability of Director is to control the secuense of the play
    
    Attributes:
        is_playing (boolean): verify and keep the game on.
        game_over (if/else): Stop the game when the user guess correctly or the player run out of guesses
        _letters_right (list[int]): Counter of the letter for the hidden word
        _puzzle: A variable that contains the class for Puzzle()
        _parachute: A variable that contains the class for Parachute()
        _get_index (list): List that contains the index of the hidden word
        _wrong_guesses (int): Counter for the wrong guesses of the player
        """
    def __init__(self):
        self._puzzle = Puzzle()
        self._parachute = Parachute()
        self._get_index = self._parachute.index_parachute()
        self._secret_word = self._puzzle.hidden_word()
        self._right_letters = []
        self._player_guess = ""
        self._wrong_guesses = -1

    def is_playing(self):
        while self.game_over() != True:
            secret_word = self._secret_word
            for letter in secret_word:
                if self._player_guess == letter and (self._player_guess not in self._right_letters):
                    self._right_letters.append(letter)
            if self._player_guess not in secret_word:
                self._wrong_guesses += 1
            for i in secret_word:
                if i in self._right_letters:
                    print(i, end=" ")
                else:
                    print("_", end=" ")
            print("\n")
            if self._wrong_guesses == 0:
                self._parachute.whole_parachute()
                self._player_guess = input("Guess a letter [a-z]: ")
            elif (self._wrong_guesses > 0 and self._wrong_guesses <= 4) and self._player_guess not in secret_word:
                self._get_index.pop(0)
                for i in self._get_index:
                    print(i)
                self._player_guess = input("Guess a letter [a-z]: ")
            elif self._wrong_guesses == 5:
                self._get_index.pop(0)
                self._get_index.insert(0, "  X")
                for i in self._get_index:
                    print(i)
            else:
                for i in self._get_index:
                    print(i)
                self._player_guess = input("Guess a letter [a-z]: ")

    def game_over(self):
        if self._get_index[0] == "  X":
            print("Game Over")
            return True
        else:
            return False

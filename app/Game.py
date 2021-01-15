
from random import choice

from Alphabet import Alphabet

class Game:

    def __init__(self, random_bool=False):

        self.random_bool = random_bool
        self.alphabet = Alphabet()
        self.letters = list(alphabet.keys())

        if self.random_bool:
            self.letter = choice(self.letters)
        else:
            self.letter = self.letters[0]

    def get_next_letter(self):

        if self.random_bool:
            self.letter = choice(self.letters)
        else:
            self.letter = self.letters[self.letters.index(self.letter) + 1]


from random import choice, shuffle

from Alphabet import Alphabet
from Words import Words

class Game:

    def __init__(self, random_bool=False):

        self._random_bool = random_bool
        self._alphabet = Alphabet()
        self._letters = list(self._alphabet.keys())
        self._words = Words()

        if self._random_bool:
            self._letter = choice(self._letters)
        else:
            self._letter = self._letters[0]

    def get_next_letter(self):

        if self._random_bool:
            self._letter = choice(self._letters)
        else:
            self._letter = self._letters[self._letters.index(self._letter) + 1]

    def get_choices(self):

        # get multple choices
        choices = self._words.get_word_choices(self._letter) + [self._alphabet[self._letter]]

        # randomize order of choices
        shuffle(choices)

        # return choices
        return choices

    def check_answer(self):

        pass

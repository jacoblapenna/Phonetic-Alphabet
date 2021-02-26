from random import choice, shuffle

if __name__ == __file__.split('/')[-1].split('.')[0] or __name__ == "__main__":
    from Alphabet import Alphabet
    from Words import Words
else:
    from .Alphabet import Alphabet
    from .Words import Words

class Game:

    def __init__(self, random_bool=False, alphabet=None, words=None):

        self._random_bool = random_bool
        if alphabet:
            self._alphabet = alphabet
        else:
            self._alphabet = Alphabet()
        self._letters = list(self._alphabet.keys())
        if words:
            self._words = words()
        else:
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

    def get_letter(self):

        return self._letter

    def get_choices(self):

        # get multple choices
        choices = self._words.get_word_choices(self._letter) + [self._alphabet[self._letter]]

        # randomize order of choices
        shuffle(choices)

        # return choices
        return choices

    def check_answer(self, answer):

        correct_answer = self._alphabet[self._letter]

        if answer == correct_answer:
            return True
        else:
            return False

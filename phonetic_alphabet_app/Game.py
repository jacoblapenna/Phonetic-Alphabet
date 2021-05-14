from random import choice, shuffle

if __name__ == __file__.split('/')[-1].split('.')[0] or __name__ == "__main__":
    from Alphabet import Alphabet
    from Words import Words
else:
    from .Alphabet import Alphabet
    from .Words import Words

class Game:

    def __init__(self):

        self._alphabet = Alphabet()
        self._letters = list(self._alphabet.keys())
        self._words = Words()

    def get_next_question(self, order, current_letter):

        if order == "random":
            letter = choice(self._letters)
        elif order == "alphabetical":
            if current_letter and current_letter in self._letters:
                try:
                    letter = self._letters[self._letters.index(current_letter) + 1]
                except IndexError:
                    letter = self._letters[0]
            else:
                letter = self._letters[0]
        else:
            return "bad_request"

        return {"letter" : letter, "choices" : self.get_choices(letter)}

    def get_choices(self, letter):

        # get multple choices
        choices = self._words.get_word_choices(letter) + [self._alphabet[letter]]

        # randomize order of choices
        shuffle(choices)

        # return choices
        return choices

    def check_answer(self, answer, letter):

        correct_answer = self._alphabet[letter]

        if answer == correct_answer:
            return True
        else:
            return False

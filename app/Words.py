
class Words(dict):
    """
    dictionary object with each letter in the alphabet containing a list
    of all the eglish words starting with that letter, as well as the number
    of words in the word list for each letter. The words are from the nltk
    corpus "words" download.
    """

    def __init__(self):
        # create words dictionary object
        self.__words = self.generate_word_dict()
        super().__init__(self.__words)

    def generate_word_dict(self):
        # create empty dict object to build on
        word_dict = {}
        # open text file with english words (downloaded from nltk)
        with open("static/en", 'r') as word_file:
            for w in word_file:
                # strip whitespace, \n character, and capitalize first letter
                word = w.strip().title()
                # grab first character
                c = word[0]
                if c not in word_dict.keys():
                    # if character isn't in dict, put it in
                    word_dict[c] = [0, []]
                else:
                    # otherwise increase word count for character entry
                    word_dict[c][0] += 1
                    # and insert new word into list under character
                    word_dict[c][1].append(word)
        # return the dict object when done
        return word_dict

# List: creates a list from a string
import re

class List:

    def __init__(self):
        self.__list = list()

    @property
    def list(self):
        return self.__list

    @list.setter
    def list(self, str):
        self.str = str
        self.__list = self.__build_list(self.str)

    def build_list(self, str):
        self.str = str
        return self.str.split()


# WordList: creates a list of words from the user's input string
# Then parses the string, making it alphabetized, lowercase, and removes
# non-alpha characters
class WordList(List):

    def __init__(self):
        self.__word_list = list()

    @property
    def word_list(self):
        return self.__word_list

    @word_list.setter
    def word_list(self, str):
        self.str = str
        self.__word_list = self.__build_word_list(self.str)

    def __build_word_list(self, str):
        self.str = str.lower()
        # regex expression that removes all characters that are not lower case alpa
        temp = re.sub('[^a-z ]+', '', self.str)
        word_list = self.build_list(temp)
        word_list.sort()

        for n in word_list:
            print(n)
        return word_list

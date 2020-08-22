import sys
sys.path.append("../sourceCode")
from word_list import WordList as WL
from word_index import WordIndex as WI

class IndexUtility:

    def __init__(self):
        self.__word_dict = dict()

    @property
    def word_dict(self):
        return self.__word_dict

    @word_dict.setter
    def word_dict(self, str):
        self.str = str
        self.__word_dict = self.__build_dict(self.str)


    def __build_dict(self, str):
        self.str = str
        word_list = WL()
        word_list.word_list = self.str
        word_dict = WI()
        word_dict.word_index = word_list.word_list
        return word_dict.word_index

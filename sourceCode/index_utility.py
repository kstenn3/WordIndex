import sys
sys.path.append("../sourceCode")
from word_list import WordList as WL

class IndexUtility:

    def __init__(self):
        self.__word_dict = dict()

    @property
    def word_dict(self):
        return self.__word_dict

    @word_dict.setter
    def word_dict(self, str):
        self.str = str
        self.__word_dict = self.__build_dic(self.str)

    def __build_index(self, word_list):
        pass

    def __index_count(self, word_index):
        pass

    def __build_dic(self, str):
        self.str = str
        word_list = WL()
        word_list.word_list = self.str
        # TODO: working on word_index right now
        word_index = self.__build_index(word_list)
        count_index = self.__index_count(word_index)
        return count_index

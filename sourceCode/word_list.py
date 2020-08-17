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


    # __build_word_list(): Build a list of words then parse it taking non alpha
    #   elements, changing all to lower case and alphabetize.
    def __build_word_list(self, str):
        self.str = str.lower()
        word_list = self.build_list(self.str)
        word_list.sort()
        return word_list

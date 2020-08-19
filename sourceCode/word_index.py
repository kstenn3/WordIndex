class WordIndex:
    # constructor
    def __init__(self):
        self.__word_index = dict()

    # getter
    @property
    def word_index(self):
        return self.__word_index

    # setter
    @word_index.setter
    def word_index(self, word_list):
        self.word_list = word_list
        self.__word_index = self.__build_index(self.word_list)

    def __count_index(self, count_dict):
        self.count_dict = count_dict
        index_dict = {}

        for key, value in self.count_dict.items():
            index_dict[key] = (len(value), value)

        return(index_dict)

    def __build_index(self, word_list):
        self.word_list = word_list
        word_dict = {}

        # alpha : num
        for n in range(len(self.word_list)):
            word_dict[n] = self.word_list[n]

        word_index = {}
        for key, value in word_dict.items():
            if value not in word_index:
                word_index[value] = [key]
            else:
                word_index[value].append(key)
        final_dict = self.__count_index(word_index)
        return final_dict

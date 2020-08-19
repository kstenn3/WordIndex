# ReadText: Reads in text from stdin. If user inputs a text file, the class will
# open the file and turned the text into a list.
class ReadText:

    def __init__(self):
        self.__text = str()

    @property
    def text(self):
        return self.__text

    # TODO set error checking in here
    @text.setter
    def text(self, input):
        if input == '':
            raise ValueError("Invalid Entry")
        self.input = input
        self.__text = self.__build_str(self.input)

    # __build_str(): checks if str is a text file. If it's a file, opens the file
    #   and converts text into a string.
    def __build_str(self, str):
        self.str = str
        if self.str[-4:] == '.txt':
            temp = ''
            with open(self.str, 'r') as reader:
                for n in reader:
                    temp += n
            self.str = temp
        return self.str

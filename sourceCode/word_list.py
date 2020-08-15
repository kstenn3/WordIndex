# text class to read in file

class WordList:
	#constructor
	def __new__(cls, text, *args, **kwargs):
		# checks if text is a file that needs to be open and read
		if text[-4:] == '.txt':
			with open(text, "r") as file:
				word_list = file.read().replace('\n', '')
		else:
			word_list = text

		return word_list

	def __init__(self, word_list, word_index = 1):
		self.word_list = word_list
		self.word_index = word_index

	# setters

	# getters

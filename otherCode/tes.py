from sys import argv

file = "wordDoc.txt"

with open (file, "r") as text:
    word_list = text.read()


print(word_list[-1])

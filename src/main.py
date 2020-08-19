#! /usr/bin/python3
import sys
sys.path.append("../sourceCode/")
from read_input import ReadText as RT
from index_utility import IndexUtility as IU

# TODO: Comment entire program
def print_index(word_dict):
    count = 1
    for key, value in word_dict.items():
        word = key + ':'
        temp =''
        for n in word_dict[key][1]:
            temp += '{} '.format(str(n))
        loc = temp.replace(' ', ', ')
        print('{}.  {:<20s} qty = {:<10d} locations = {}'.format(count, word, word_dict[key][0], loc[:-2]))
        count =+ count + 1



def main():
    user_input = RT()
    user_input.text = input('> ')

    word_index = IU()
    word_index.word_dict = user_input.text
    print_index(word_index.word_dict)

# TODO: Error Checking: research good error checking, add try/catches
# TODO: refactor program


if __name__ == '__main__':
        main()

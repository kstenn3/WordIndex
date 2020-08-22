#! /usr/bin/python3
import sys
sys.path.append('classes/')
sys.path.append('modules/')
from read_input import ReadText as RT
from index_utility import IndexUtility as IU
from results_mod import print_index, make_file

# TODO: Comment entire program
def main():
    user_input = RT()
    user_input.text = input('> ')

    word_index = IU()
    word_index.word_dict = user_input.text
    make_file(word_index.word_dict, user_input.text)
# TODO: Error Checking: research good error checking, add try/catches
# TODO: refactor program: research how to


if __name__ == '__main__':
        main()

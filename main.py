#! /usr/bin/python3
import sys
sys.path.append('src/modules/')
sys.path.append('src/classes/')
from read_input import ReadText as RT
from index_utility import IndexUtility as IU
from results import print_index, create_file


def main():
    user_input = RT()

    # check input is not blank
    while True:
        try:
            user_input.text = input('> ')
            assert len(user_input.text) > 0
        except AssertionError:
            print('Input can not be empty.')
        else:
            break

    word_index = IU()
    word_index.word_dict = user_input.text

    create_file(word_index.word_dict, user_input.text)
    print("Word Index Complete")


if __name__ == '__main__':
        main()

#! /usr/bin/python3
import sys
sys.path.append("../sourceCode/")
from read_input import ReadText as RT
from index_utility import IndexUtility as IU

def main():

    user_input = RT()
    user_input.text = input('> ')

    word_index = IU()
    word_index.word_dict = user_input.text










if __name__ == '__main__':
        main()

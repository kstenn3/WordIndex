# TODO: add programmer info and program details
from word_list import WordList
def main():

    print("""
        < WELCOME TO WORD INDEX UTILITY >

        insert a file name or input text
        """)
    text = input('> ')

    word_index = WordList(text)




if __name__ == '__main__':
        main()

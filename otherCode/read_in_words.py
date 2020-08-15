#! /usr/bin/python3

# get_text(): reads in text from file or stdin, thens stores words in a list
def get_text(file_name):
    temp_list = ''
    if file_name[-4:] == '.txt':
        list = ''
        with open(file_name, 'r') as reader:
            for n in reader:
                list = list + n
        temp_list = list.split()
    else:
        temp_list = file_name.split()
    return temp_list

# get_location(): gives each word in a list a location
def get_loc(word_list):
    # word_index = { i + 1 : word_list[i] for i in range(0, len(word_list))}
    word_index = {}
    index = 1
    for n in word_list:
        word_index[index] = n
        index = index + 1
    return word_index

# print_list(): prints out a word index
def print_list(list):
    for x, y in list.items():
        print(f"{x} : {y}")



# main(): runs word index program
# read from standard in and print each word separately
def main():
    user_input = input('> ')
    word_list = get_text(user_input)
    word_index = get_loc(word_list)
    print_list(word_index)
    
# TODO: practice on the fundamentals in this script
# TODO: Refactor the code
# TODO: error handling, try and catch


if __name__ == '__main__':
    main()

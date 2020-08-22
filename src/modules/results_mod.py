import os

def make_file(word_dict, user_input):
    file_name = 'user_input_results.txt'

    if os.path.exists(file_name):
        x = input('remove file? {} '.format(file_name))
        if x.lower() == 'yes' or x.lower() == 'y':
            os.remove(file_name)
        else:
            print('good bye')
            exit()

    f = open(file_name, 'a')
    count = 1
    for key, value in word_dict.items():
       word = key + ':'
       temp = ''
       for n in word_dict[key][1]:
           temp += '{} '.format(str(n))
       loc = temp.replace(' ', ', ')
       f.write('{}.  {:<20s} qty = {:<20d} locations = {}\n'.format(count, word, word_dict[key][0], loc[:-2]))
       count =+ count + 1
    f.close()


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

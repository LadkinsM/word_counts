"""Count words in file."""

from sys import argv

def tokenize(filename):
    '''Return a list of words from the file at filename.'''
    # data = open(filename)
    data=filename
    words_list=[]
    # for line in data:
    #     words = line.rstrip().split(" ")
    for line in data:
        line = line.rstrip()
        words = line.split(' ')
        for word in words: 
            word=word.replace(',', '').replace('?','').replace('.','')
            words_list.append(word.lower())

    return words_list

def count_words(words_list):
    '''Take in a list of strings and return a dictionary of each string and the number of tiems it appears in the list.'''
    all_words = {}
    for word in words_list:
        all_words[word] = all_words.get(word, 0) + 1

    return all_words

def print_word_counts(word_counts):
    '''Take in a dictionary of word counts and print each key and value from the dictionary.'''
    for word, count in word_counts.items():
        print(f"{word} {count}")

def run_word_counts(filename):
    data = open(filename)
    words_list = tokenize(data)
    all_words = count_words(words_list)
    word_counts = print_word_counts(all_words)

run_word_counts(argv[1])

# def word_counts(filename, filename2):
#     data = open(filename)
#     all_words = {}
#     for line in data:
#         words = line.rstrip().split(" ")
#         for word in words:
#             all_words[word] = all_words.get(word, 0) + 1
#     for word, count in all_words.items():
#         print(f'{word} {count}')

# word_counts(argv[1])
    


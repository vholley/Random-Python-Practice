"""
scrabble.py

This program contains functions to help find words in the Official Scrabble
Player's Dictionary, Second Edition (dictionary.txt):

length_n(file_name, n): returns an list of all words of length n.

starts_with(file_name, n, first_letter): returns a list of all words of length
n beginning with the letter first_letter

contains_letter(file_name, n, included): returns a list of all words of length
n containing the letter included but not beginning with it.

vowel_heavy(file_name, n, m): returns a list of all words of length n with at
least m vowels.
"""


def length_n(file_name, n):

    # Create a list to append words to and be returned by the function
    word_list = []

    # Open the dictionary text file and make it readable
    dictionary_file = open(file_name, 'r')

    # Read the first word of the dictionary and remove the newline character
    word = dictionary_file.readline().rstrip('\n')

    # Read the rest of the file
    while word != '':
        # If the length of the word (without a newline character) on the
        # current line is n, append it to word_list
        if len(word) == n:
            word_list.append(word)

        # Then read the next line and remove the newline character
        word = dictionary_file.readline().rstrip('\n')

    # Close the dictionary file
    dictionary_file.close()

    return word_list


length_n('dictionary.txt', 22)


def starts_with(file_name, n, first_letter):

    # Create a list to append words to and be returned by the function
    word_list = []

    # Open the dictionary text file and make it readable
    dictionary_file = open(file_name, 'r')

    # Read the first word of the dictionary and remove the newline character
    word = dictionary_file.readline().rstrip('\n')

    # Read the rest of the file
    while word != '':
        # If the length of the wordon the current line is n and the first
        # letter is first_letter, append it to word_list
        if len(word) == n and word[0] == first_letter:
            word_list.append(word)

        # Then read the next line and remove the newline character
        word = dictionary_file.readline().rstrip('\n')

    # Close the dictionary file
    dictionary_file.close()

    return word_list


starts_with('dictionary.txt', 3, 'z')


def contains_letter(file_name, n, included):

    # Create a list to append words to and be returned by the function
    word_list = []

    # Open the dictionary text file and make it readable
    dictionary_file = open(file_name, 'r')

    # Read the first word of the dictionary and remove the newline character
    word = dictionary_file.readline().rstrip('\n')

    # Read the rest of the file
    while word != '':
        # If the length of the word on the current line is n, the word contains
        # the included letter, and the word does not begin with the included
        # letter, append it to word_list
        if len(word) == n and word[0] != included and included in word:
            word_list.append(word)

        # Then read the next line and remove the newline character
        word = dictionary_file.readline().rstrip('\n')

    # Close the dictionary file
    dictionary_file.close()

    return word_list


contains_letter('dictionary.txt', 3, 'z')


def vowel_heavy(file_name, n, m):

    # Use a list of vowels to check against (upper and lowercase to be thorough
    # for other dictionaries)
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

    # Create a list to append words to and be returned by the function
    word_list = []

    # Open the dictionary text file and make it readable
    dictionary_file = open(file_name, 'r')

    # Read the first word of the dictionary and remove the newline character
    word = dictionary_file.readline().rstrip('\n')

    # Read the rest of the file
    while word != '':

        # Count the number of vowels in the word
        count = 0
        for char in word:
            if char in vowels:
                count += 1

        # If the length of the word on the current line is n and the word
        # contains m or more vowels, append to word_list
        if len(word) == n and count >= m:
            word_list.append(word)

        # Then read the next line and remove the newline character
        word = dictionary_file.readline().rstrip('\n')

    # Close the dictionary file
    dictionary_file.close()

    return word_list


vowel_heavy('dictionary.txt', 5, 4)

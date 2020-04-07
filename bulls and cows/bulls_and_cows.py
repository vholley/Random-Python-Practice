'''
bulls_and_cows.py

This program contains functions for game.py. Further explaination in the
readMe.txt
'''


import random


def generate_secret():
    ''' Generates a 4 digit number with no repeat digits.
    It converts the number to a string and returns it.'''
    secret = random.sample(range(10), 4)

    secret = ''.join(map(str, secret))

    return secret


def how_many_bulls(answer, guess):
    '''Returns the number of bulls that the guess earns when the
    secret number is answer. Both answer and guess should be strings.'''
    bulls = 0

    # Compare each digit of answer with the corresponding digit of guess
    for element in range(len(guess)):
        if answer[element] == guess[element]:
            bulls += 1

    return bulls


def how_many_cows(answer, guess):
    '''Returns the number of bulls that the guess earns when the
    secret number is answer. Both answer and guess should be strings'''
    cows = 0

    # Check if each element of the answer is in the guess
    for element in range(len(guess)):
        if answer[element] in guess:
            cows += 1

    # Exclude the number of bulls from the cows count
    cows = cows - how_many_bulls(answer, guess)

    return cows

'''
game.py

This program runs the game Bulls and Cows. Further explaination is
in the readMe.txt
'''

import bulls_and_cows as bc


def main():
    print('Welcome to Bulls and Cows!')
    again = 'y'
    while (again == 'y'):
        play_game()
        again = input('Would you like to play again? (y/n)  ')
    print('So long sucker!')


def play_game():
    ''' Plays one interactive game of bulls and cows on the console'''

    # Run generate_secret to create the computer's number, answer
    answer = bc.generate_secret()

    # When the game is over, end_game = T, otherwise end_game = F
    end_game = 'F'

    # Count the number of guesses, guess_counter
    guess_counter = 0

    # Continue running the game until the player's guess matches the answer
    while end_game == 'F':

        # Take input from the player for the guess, guess
        guess = input('Enter your guess.  ')

        # Increment the number of guesses
        guess_counter += 1

        # If the answer matches the guess, end the game
        if answer == guess:
            print('Congratulations, you win!')
            print('Number of guesses: ' + str(guess_counter))
            end_game = 'T'

        # If the answer does not match, print the number of bulls and cows
        else:
            bulls = str(bc.how_many_bulls(answer, guess))
            cows = str(bc.how_many_cows(answer, guess))

            print('Number of bulls: ' + bulls)
            print('Number of cows: ' + cows)


# Call the main function to run the game
main()

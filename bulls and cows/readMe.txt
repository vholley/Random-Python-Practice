game.py

The game uses the given main() function to initiate the game and call play_game().


play_game()

play_game() uses generate_secret() to create a hidden number for the computer.
play_game() then takes a guess of four digits from the player (this program
assumes that the player input will always be correct). If the inputted guess does
not match the hidden number, then the play_game() displays the number of bulls
and cows (the number of digits in the correct position and the number of digits
which are otherwise present in the hidden number, respectively), found using the
functions how_many_bulls() and how_many_cows(). This loops until the inputted 
guess matches the hidden number exactly, displaying the number of guesses, terminating
the loop, and exiting play_game().



bulls_and_cows.py

This contains the functions used by play_game()


generate_secret()

This uses random.sample() to generate four random, nonrepeating numbers from
0 to 9. Then the list is joined to a string which is the output.


how_many_bulls()

This takes an input of two strings, one for the hidden number and one for the
player's guess. For each element in the guess string, it checks if the element
in that position matches the element of the answer string. It then counts how
many times this occurs and outputs the number of occurences.


how_many_cows()

This takes an input of two strings, one for the hidden number and one for the
player's guess. For each element in the guess string, it checks if the element
in the corresponding position of the answer string is found in the guess string
and counts how many times this occurs. In order to prevent double counting of
bulls, the number of bulls is subtracted from the count of the number of cows.
This is made easy because both functions take the exact same inputs.
how_many_cows() then outputs the remaining number of occurences.
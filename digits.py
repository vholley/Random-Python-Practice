'''
digits.py

This program takes the input of a nine digit number with no duplicates and
returns the next largest number with those digits, if possible.
'''

# Take a nine digit number as input (this program assumes a correct input)
input_str = input('Please enter nine digit number, without duplicates.  ')

# Put the input into a list with each digit as an element
input_list = list(input_str)

# Take the length of input_list from the right to be able to create a range
input_len = len(input_list) * -1

# Starting on the right side and moving left, check each digit until one is
# reached which is smaller than the previous, then stop.
input_range = range(-1, input_len, -1)  # range(start, end, step)

for i in input_range:
    if input_list[i] > input_list[i-1]:
        break

# Set the stop position to i - 1 and create a variable for its value
stop_pos = i - 1

stop_val = input_list[stop_pos]

# If the digits are all in descending order, then there is no larger number.
if input_list == sorted(input_list, reverse=True):
    print('Not Possible')


else:

    '''
The next step is to find the smallest number in the slice to the right of the
stop position that is larger than stop_val. This will be done by creating a new
list from a slice of input_list and sorting it numerically.
    '''

# Create a list of values from the slice to the right of stop_pos
    right_list = input_list[-1:stop_pos:-1]

    right_len = len(right_list)

# Sort right_list numerically in ascending order
    right_list.sort()

# Find the lowest number in right_list that is larger than stop_val, then stop
    right_range = range(0, right_len + 1)

    for j in right_range:
        if right_list[j] > stop_val:
            break

# Create variables for the value and position of the number that was found
    swap_val = right_list[j]

    swap_pos = input_list.index(swap_val)

# Switch the value at the stop position with the swap value.
    input_list[stop_pos] = swap_val

    input_list[swap_pos] = stop_val

# Sort all values currently in the slice to the right of stop_pos
    input_list[stop_pos + 1:] = sorted(input_list[stop_pos + 1:])

# Create the output from input_list by appending the list elements to a string
    output = ''  # an empty string to append the list elements into

    for elements in input_list:
        output += elements

# Print the output
    print('The next largest number with those digits is', output)

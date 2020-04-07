'''
time.py

This program takes an input for the current time and an input for a number of
hours to wait and outputs the time after the wait.
'''

# Take inputs for the current time and the number of hours to wait
current_time_str = input('What is the current time (in 24 hour format)?    ')
wait_time_str = input('How many hours do you have to wait?    ')

# Cast the inputs from strings to integers
current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

# Calculate the sum of the current time and the wait
total_hours = current_time_int + wait_time_int

# Calculate the time after the wait using the remainder after dividing by 24
output_time = total_hours % 24

# Output the time in 24 hours format
print(output_time)

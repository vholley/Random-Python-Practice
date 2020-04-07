"""
hamming.py

This program computes the Hamming distance between two binary strings.
"""


binary_one = '0010100'
binary_two = '1010010'

binary_one_list = list(binary_one)
binary_two_list = list(binary_two)

binary_one_len = len(binary_one_list)

binary_range = range(0, binary_one_len)

hamming = 0

for i in binary_range:
    if binary_one_list[i] != binary_two_list[i]:
        hamming += 1


print(hamming)

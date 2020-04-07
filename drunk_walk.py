# -*- coding: utf-8 -*-
"""
drunk_walk.py

This program simulates a person walking in one of four random directions,
beginning at cartesian coordinates (0,0) and gives the end coordinates and how
many units the person moved away from the initial position.
"""
import random

x = 0  # initial x position
y = 0  # initial y position

sum_range = range(1, 101)

for i in sum_range:
    direction = random.randint(1, 4)  # either left/right/up/down

    if direction == 1:  # randomly move up
        x += 1

    elif direction == 2:  # randomly move down
        x -= 1

    elif direction == 3:  # randomly move right
        y += 1

    elif direction == 4:  # randomly move left
        y -= 1

print('The drunkard is at (' + str(x) + ',' + str(y) + ').')

distance = abs(x) + abs(y)

print('The drunkard moved', str(distance), 'units.')

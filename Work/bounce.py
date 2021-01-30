#!/bin/python

# bounce.py
#
# Exercise 1.5

height = 100.0
count = 1

while round(height, 4) > 0:
    print(f'Bounce #{count} from {round(height, 4)}M')
    count += 1
    height *= 0.6

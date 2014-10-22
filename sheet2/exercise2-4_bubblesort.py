# -*- coding: utf-8 -*-
"""
This program first creates a random number sequence. Then, we use the
Bubblesort algorithm to sort this sequence.

Author: Johannes, October 2013
"""

import random

# Create a list of n random numbers between 1 and 20
n = 10
numbers = []
for i in range(n):
    random_number = random.randint(1, 20)
    numbers.append(random_number)

print "The unsorted number sequence:", numbers

# Track if there was any interchange in one iteration of the while loop
interchanged = True

while interchanged:
    interchanged = False
    for i in range(n-1):
        # If left number is bigger than right number, interchange those
        if numbers[i] > numbers[i+1]:
            tmp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = tmp
            interchanged = True

print "The sorted number sequence:", numbers

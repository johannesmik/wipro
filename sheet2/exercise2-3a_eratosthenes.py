# -*- coding: utf-8 -*-
"""
Calculate a list of prime numbers using the "Sieve of Eratosthenes" method.

This is the most basic method, without any optimizations.

It needs 146 markings to find the 25 primes in the interval [1, 100].

Author: Johannes, October 2013
"""

n = 100
marked = [False] * (n+1)

# To count the number of markings
markings = 0

# Mark the numbers 0 and 1 as they are surely not prime
marked[0] = True
marked[1] = True

for i in range(2, n+1):
    # Smallest not marked number
    if marked[i] == False:
        # Mark all multiples
        for k in range(i*2, n+1, i):
            marked[k] = True
            markings += 1

# Save the found primes in a list
primes = []
for number, mark in enumerate(marked):
    if mark == False:
        primes.append(number)

# Output
print primes
print "We needed ", markings, " markings to find ", len(primes), " primes."

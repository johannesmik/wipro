"""
This program prints the numbers from 1 to 100.
It prints bizz, buzz, and/or woof if the number is divisible by 3, 5, and/or 7 correspondingly.

Author: Johannes, October 2014
"""

for i in range(1, 101):
    if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print i
    else:
        if i % 3 == 0:
            print "bizz",
        if i % 5 == 0:
            print "buzz",
        if i % 7 == 0:
            print "woof",
        print ""            # begin a new line

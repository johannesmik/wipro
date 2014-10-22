"""
This program calculates the square root of the variable 'a'.
It uses the iterative method mentioned on the exercise sheet.

Author: Johannes, October 2014
"""

# We want the root of this number
a = 100

# We keep track of our x-values in a list.
# x[-1] returns the last value.
x = [1]

# Precision
eps = 0.00001

while abs(x[-1] ** 2 - a) > eps ** 2:

    # Calculate the next x-value (formula on exercise sheet)
    next_x = 0.5 * (x[-1] + a / x[-1])
    x.append(next_x)

    print x  # Print the list of x-values, so we can follow the behavior

print "Die Wurzel von ", a, " ist ", x[-1]

# Now plot the list of x

import matplotlib.pyplot as plt

plt.plot(x)
plt.show()

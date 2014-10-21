import math
import random

p_circle = 0
p_total = 1000

for i in range(p_total):
    x = random.random()
    y = random.random()

    if math.sqrt(x**2 + y**2) <= 1:
        p_circle += 1

print "The approximation of pi is: ", 4 * float(p_circle) / p_total

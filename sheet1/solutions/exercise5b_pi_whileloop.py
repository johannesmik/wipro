import random
import math

p_circle = 0    # Number of points in the circle
p_total = 0     # Number of points generated
pi_approx = 0.0
epsilon = 0.0001

while ( abs ( pi_approx - math.pi ) > epsilon ):
    p_total += 1
    x = random.random()
    y = random.random()
    if math.sqrt(x ** 2 + y ** 2) <= 1.0 : # point is in the circle
        p_circle += 1
        pi_approx = float ( p_circle )/ p_total * 4
print "Pi : %f and Math.pi is %f ( Points generated : %d ) " \
           % ( pi_approx , math . pi , p_total )

import math

# a) Area of a circle

r = 5.0
A = r ** 2 * math.pi
print "A circle of radius", r, "has an area of", A

# b) quadratic equation

a = 0.2
b = 2.0
c = 1.0

x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print "x1 is", x1, "and x2 is", x2

print "Test:"
print a, "*", x1, "**2 +", b, "*", x1, "+", c, "=", a * x1 ** 2 + b * x1 + c
print a, "*", x2, "**2 +", b, "*", x2, "+", c, "=", a * x2 ** 2 + b * x2 + c

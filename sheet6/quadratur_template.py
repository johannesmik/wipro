from __future__ import division
import math

class Quadrature:
    # TODO-3 Define this class.
    # It should implement the following methods:
    # __init__(self, a, b, n)
    # integrate(self, f)
    pass # Delete this line when you've finished your implementation

class Midpoint:
    # TODO-4 Let this class inherit from the class Quadrature.
    # It should inherit the __init__ and integrate methods from Quadrature.
    # It should implement the construct method by itself.
    # TODO-5 Do the same as in TODO-4 for class Trapezoidal. 
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def construct(self):

        # TODO-1: Replace w and x by lists depending on self.a, self.b and self.n 

        w = [0.2, 0.2, 0.2, 0.2, 0.2]
        x = [0.1, 0.3, 0.5, 0.7, 0.9]

        return x, w

    def integrate(self, f):
        x, w = self.construct()

        summe = 0
        for i in range(self.n):
            summe += w[i] * f(x[i])

        return summe

class Trapezoidal:
    # TODO-2: Now do the same for the Trapezoidal method
    # Hint: you can copy most of the code from Midpoint
    pass # Delete this line when you've finished your implementation

t = Midpoint(0, 1, 5)
print "Midpoint Integration von Sinus: ", t.integrate(math.sin)


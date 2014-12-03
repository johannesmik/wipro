from __future__ import division
import math

class Midpoint:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def construct(self):
        # TODO-1: Replace w and x by lists depending on self.a, self.b and self.n
        # (Formula derived on blackboard) 
        w = [0.25, 0.25, 0.25, 0.25]
        x = [0.125, 0.375, 0.625, 0.875]

        return x, w

    def integrate(self, f):
        x, w = self.construct()
        summe = 0
        for i in range(self.n):
            summe += w[i] * f(x[i])
        return summe

# TODO-2: Now do the same for a new Trapezoidal Class
# Hint: you can copy most of the code from Midpoint

t = Midpoint(0, 1, 5)
print "Midpoint Integration von Sinus: ", t.integrate(math.sin)


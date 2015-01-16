### Fitting a polynomial

Like in exercise sheet 10, we can simply fit a polynom (of arbitrary degree) through some datapoints using `numpy.polyfit`.

```python
import numpy as np
import matplotlib.pyplot as plt

def polyval(a, x):
    """ Evaluates a polynom with coefficients 'a' at the point x. """
    sum = 0
    n = len(a)
    for i in range(n):
        sum += a[n-1-i] * x ** i
    return sum

# Define the datapoints
x1 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
x2 = [1, 2, 1.5, 2, 3, 2.5, 4]

# Find the coefficients
poly_degree = 1
a = np.polyfit(x1, x2, poly_degree)

# Plot the datapoints
plt.scatter(x1, x2)

# Plot the found polynom
x = np.arange(0, 8, 0.05)
y = polyval(a, x)
plt.plot(x, y)

plt.show()
```

The documentation about `polyfit` can be found [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyval.html).

__author__ = 'johannes'
import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

def poly(x, a):
    " Returns a0 + a1*x + a2*x**2 + a3*x**3 + ... + aN*x**N "
    sum = 0 *x
    for ai, i in zip(a, range(len(a))):
        sum += ai*(x**i)
    return sum

def vandermode(data):
    # n: datapoints, d: dimensions
    n, d = data.shape

    # Build up Vandermode Matrix
    V = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            V[i,j] = data[i,0]**(n-j-1)
    b = data[:,1]
    a = scipy.linalg.solve(V, b)
    a = a[::-1]
    # Important! Reverse array a

    return a


def plot():
    # Unsere Daten
    data = np.array([[1,1], [2,2], [3,1.5], [4,2], [5,3], [6,2.5], [7,4]])

    # Scatter plot for our data
    plt.scatter(data[:,0], data[:,1], s=100, c='g', marker='x')

    # Vandermode
    a_v = vandermode(data)
    x_v = np.linspace(0, 8, 100)
    y_v = poly(x_v, a_v)
    plt.plot(x_v, y_v, 'b', label='Vandermode', linewidth=2)

    # Polyfit
    a_p = np.polyfit(data[:,0], data[:,1], 6)
    a_p = a_p[::-1] # They have to be reversed too
    x_p = x_v
    y_p = poly(x_p, a_p)
    plt.plot(x_p, y_p, 'r--', label='Polyfit', linewidth=2)
    plt.legend()
    plt.show()

plot()

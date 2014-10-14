__author__ = 'johannes'
import scipy.optimize
from mpl_toolkits.mplot3d import Axes3D     #3D Axes
from matplotlib import cm                   #Colormaps
import matplotlib.pyplot as plt
import numpy as np

# List, where the iteration steps can be saved
iteration_steps = []

def rosenbrock(x):
    " The Rosenbrock function "
    # TODO define Rosenbrock
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2
    # What is so cool about this?

def f(x):
    " Save position x as an iteration step "
    iteration_steps.append(x)

def optimize_rosenbrock():
    start = [-0.2, 2.5]
    iteration_steps = []

    # TODO call the optimization function
    x_opt = scipy.optimize.fmin(rosenbrock, start, callback=f)
    print "Optimum point:  f(%.3f, %.3f) = %.3f" % (x_opt[0], x_opt[1], rosenbrock(x_opt))

def plot_rosenbrock():
    fig = plt.figure()

    # Prepare data: Rosenbrock function
    ax = fig.gca(projection='3d')
    X = np.arange(-1.5, 1.5, 0.1)
    Y = np.arange(-0.5, 3, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = rosenbrock([X, Y])

    # Prepare data: Iterations Steps
    iteration_steps_array = np.array(iteration_steps)
    x_i = iteration_steps_array[:,0]
    y_i = iteration_steps_array[:,1]
    z_i = rosenbrock([x_i, y_i])

    # Plot the Rosenbrock function
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.cool,
            linewidth=0, antialiased=False)

    # Plot the iteration steps
    ax.plot(x_i, y_i, z_i, c='r')

    # Set some axis properties
    #ax.set_zlim(0, 1200)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")

    plt.show()

optimize_rosenbrock()
plot_rosenbrock()

"""
PARC: Point Arc
"""

import numpy as np
import matplotlib.pyplot as plt

def arc():
    circular_arc()


def circular_arc():
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.grid(True)

    plt.axis([-150, 150, -150, 150])
    plt.axis('on')
    plt.grid(True)

    # x and y offsets from origin
    xc = 17
    yc = 17
    # radium determines length of curve
    r = 23
    # ——————————————————————————————————————————plot arc

    start_angle = 6
    end_angle = 78

    start_angle_rad = start_angle * np.pi / 180
    end_angle_rad = end_angle * np.pi / 180
    dp = (end_angle_rad - start_angle_rad) / 100

    # make empty numpy array for two point list, 1 x 2
    # first arg is rows, second arg is cols
    points = np.empty((1,2))
    print(points)


    # draws the arc
    for incr_angle_rad in np.arange(start_angle_rad, end_angle_rad, dp):
        x = xc + r * np.cos(incr_angle_rad)
        y = yc + r * np.sin(incr_angle_rad)
        # append points list to itself.
        # append to bottom by putting new list in first arg
        # append to top by putting new list in second arg
        # third arg is axis. Append to row with axis=0, cols with axis=1
        points = np.append(np.array([[x,y]]), points, axis=0)
        print(points[0])
        # using original x,y values
        plt.scatter(x, y, s=1, color='g')
        # using numpy array
        # plt.scatter(points[0][0], points[0][1], s=1, color='b')

    print('- + - + - + - + - + - + - + - + - + ')

    # delete default values [0, 0] created at initialization
    # default will be at bottom (last index)
    # first arg is original array, second arg, is target index
    # third arg is target dimension. For 2d array, 0 is rows, 1 is cols
    points = np.delete(points, len(points)-1,0)

    # element wise operation
    points = np.add(points, -30)
    ''' for our example, -30 = a
    [[x1,y1]     [[a, a]     [[x1+a, y1+a]
       ...    +   ...     =        ...
     [xn,yn]]     [a, a]]     [xn+a, yn+a]]
    ''' # addition occurs with arrays of the same size and is commutative

    for point in points:
        plt.scatter(point[0], point[1], s=1, color='b')


    for point in points:
        print(point)

    print('- + - + - + - + - + - + - + - + - + ')


    # print to see structure of Numpy array
    print(points)


    # ———————————————————————————————————————————labels
    # dot for center
    plt.scatter(xc, yc, s=10, color='k')
    # dot for starting points
    plt.scatter(xc + r * np.cos(start_angle_rad), yc + r * np.sin(start_angle_rad), s=10, color='r')
    plt.scatter(points[0][0], points[0][1], s=10, color='r')
    # dot for ending points
    plt.scatter(xc + r * np.cos(end_angle_rad), yc + r * np.sin(end_angle_rad), s=10, color='r')
    plt.scatter(points[len(points)-1][0], points[len(points)-1][1], s=10, color='r')
    # text for center of arc
    plt.text(xc + 4, yc - 4, '({},{})'.format(xc, yc), color='k')
    # text for start point
    plt.text(xc + r * np.cos(start_angle_rad) + 4, yc + r * np.sin(start_angle_rad) - 4, '({:.2f},{:.2f})'.format(xc + r * np.cos(start_angle_rad), yc + r * np.sin(start_angle_rad)), color='r')
    # text for end point
    plt.text(xc + r * np.cos(end_angle_rad) + 4, yc + r * np.sin(end_angle_rad) - 4, '({:.2f},{:.2f})'.format(xc + r * np.cos(end_angle_rad), yc + r * np.sin(end_angle_rad)), color='r')
    plt.show()

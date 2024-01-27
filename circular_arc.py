1
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


    xc = 17
    yc = 17
    r = 23
    # ——————————————————————————————————————————plot arc

    start_angle = 6
    end_angle = 78

    p1 = start_angle * np.pi / 180
    p2 = end_angle * np.pi / 180
    dp = (p2 - p1) / 1000

    for p in np.arange(p1, p2, dp):
        x = xc + r * np.cos(p)
        y = yc + r * np.sin(p)
        plt.scatter(x, y, s=1, color='g')

    # ———————————————————————————————————————————labels

    plt.scatter(xc, yc, s=10, color='k')
    plt.scatter(xc + r * np.cos(p1), yc + r * np.sin(p1), s=10, color='r')
    plt.scatter(xc + r * np.cos(p2), yc + r * np.sin(p2), s=10, color='r')
    plt.text(xc + 4, yc - 4, '({},{})'.format(xc, yc), color='k')
    plt.text(xc + r * np.cos(p1) + 4, yc + r * np.sin(p1) - 4, '({:.3f},{:.3f})'.format(xc + r * np.cos(p1), yc + r * np.sin(p1)), color='r')
    plt.text(xc + r * np.cos(p2) + 4, yc + r * np.sin(p2) - 4, '({:.3f},{:.3f})'.format(xc + r * np.cos(p2), yc + r * np.sin(p2)), color='r')
    plt.show()

arc()
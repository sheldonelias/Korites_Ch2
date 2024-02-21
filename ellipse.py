"""
Listing 2-7. ELLIPSES
"""

import numpy as np
import matplotlib.pyplot as plt

def ellipse_trig1():
    plt.axis([-75, 75, 50, -50])

    plt.gca().set_aspect('equal', adjustable='box')

    plt.axis('on')
    plt.grid(True)

    plt.arrow(0, 0, 60, 0, head_length=4, head_width=3, color='k')
    plt.arrow(0, 0, 0, 45, head_length=4, head_width=3, color='k')

    plt.text(58, -3, 'x')
    plt.text(-5, 44, 'y')

    # ----------------------------------horizontal red ellipse
    a = 40
    b = 20
    p1 = 0
    p2 = 180 * np.pi / 180
    dp = (p2 - p1) / 180

    xplast = a
    yplast = 0
    for p in np.arange(p1, p2, dp):
        xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
        yp = np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
        if p > np.pi / 2:
            xp = -xp
        plt.plot([xplast, xp], [yplast, yp], color='r')
        plt.plot([xplast, xp], [-yplast, -yp], color='r')
        xplast = xp
        yplast = yp
        plt.show()
        pass

def ellipse_algebraic():
    plt.axis([-75, 75, 50, -50])

    plt.gca().set_aspect('equal', adjustable='box')

    plt.axis('on')
    plt.grid(True)

    plt.arrow(0, 0, 60, 0, head_length=4, head_width=3, color='k')
    plt.arrow(0, 0, 0, 45, head_length=4, head_width=3, color='k')

    plt.text(58, -3, 'x')
    plt.text(-5, 44, 'y')

    a = 20 # x-radius
    b = 40 # y-radius
    xp1 = -a # sets first angle drawing start on opposite sides
    xp2 = a
    dx = .1 # 1/10 of a unit

    xplast = -a
    yplast = 0
    for xp in np.arange(xp1, xp2, dx):
        yp = b * (1 - xp ** 2 / a ** 2) ** .5
        plt.plot([xplast, xp], [yplast, yp], linewidth=1, color='g')
        plt.plot([xplast, xp], [-yplast, -yp], linewidth=1, color='g')
        xplast = xp
        yplast = yp

    plt.plot([xplast, a], [yplast, 0], linewidth=1, color='g')
    plt.plot([xplast, a], [-yplast, 0], linewidth=1, color='g')

    plt.show()
    pass

def ellipse_disc_trig():
    plt.axis([-75, 75, 50, -50])

    plt.gca().set_aspect('equal', adjustable='box')

    plt.axis('on')
    plt.grid(True)

    plt.arrow(0, 0, 60, 0, head_length=4, head_width=3, color='k')
    plt.arrow(0, 0, 0, 45, head_length=4, head_width=3, color='k')

    plt.text(58, -3, 'x')
    plt.text(-5, 44, 'y')

    a = 5
    b = 15
    p1 = 0
    p2 = 180 * np.pi / 180
    dp = .2 * np.pi / 180

    for p in np.arange(p1, p2, dp):
        xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
        yp = np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
        if p > np.pi / 2:
            xp = -xp
        plt.plot([xp, xp], [yp, -yp], linewidth=1, color='b')

    plt.show()

#Trigonometric formula use
def ellipse_trig2():

    plt.axis([-75, 75, 50, -50])

    plt.gca().set_aspect('equal', adjustable='box')

    plt.axis('on')
    plt.grid(True)

    plt.arrow(0, 0, 60, 0, head_length=4, head_width=3, color='k')
    plt.arrow(0, 0, 0, 40, head_length=4, head_width=3, color='k')

    plt.text(58, -3, 'x')
    plt.text(-5, 40, 'y')

    # -----------------------------------------------------ellipse
    a = 50. # Sets the horizonal radius [0 to +4-60]
    b = 30. # Sets the vertical radius [0 to +/-40]
    p1 = 0 # Do not change from 0. That is the starting angle
    p2 = 180. * np.pi / 180. # Ending angle in radians. [0 to +/-180]
    dp = (p2 - p1) / 100. # Number of line parts on each top and bottom half [10-1000]

    xplast = a # Start drawing on the x-axis at value of a
    yplast = 0 # Starts drawing at y=0
    # Adds dp to angle p1 as many times to read dp + p2
    for p in np.arange(p1, p2 + dp, dp):  # try deleting the extra + dp

        # Finds x value
        xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
        # Finds y values
        yp = np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)

        # Because above two are giving absolute value, must consider negative x side.
        # If angle p is greater than 90 degrees, than position x value to the negative
        # For curiosity, try commenting the if statement out
        if p > np.pi / 2:
            xp = -xp

        # draws top half
        plt.plot([xplast, xp], [-yplast, -yp], color='b')
        # draws bottom half
        plt.plot([xplast, xp], [yplast, yp], color='k')

        # pass found value to last value so that the line can be drawn
        # where it left off
        xplast = xp
        yplast = yp

    # --------------------------------------------------------line
    plt.plot([0, 40], [0, 40], color='k')

    # -------------------------------------------------------point
    p = 45. * np.pi / 180.
    xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)
    yp = np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)
    plt.scatter(xp, yp, s=20, color='r')

    # ------------------------------------------------------labels
    plt.text(23, -3, 'a', color='k')
    plt.text(-5, 15, 'b', color='k')
    plt.text(32, 28, '(xp,yp)')
    plt.text(30, 12, 'p')
    plt.text(10, 18, 'r')

    p1 = 0
    p2 = 45 * np.pi / 180
    dp = (p2 - p1) / 180
    r = 30
    for p in np.arange(p1, p2, dp):
        x = r * np.cos(p)
        y = r * np.sin(p)
        plt.scatter(x, y, s=.1, color='r')

    plt.arrow(25, 17.5, -1, 1, head_length=3, head_width=2, color='r')

    plt.show()
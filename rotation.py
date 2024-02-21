'''
Rotation
'''

import matplotlib.pyplot as plt
import numpy as np


def np_rotz(xc, yc, xp, yp, rz):  # ——–xp,yp=un-rotated coordinates relative to xc,yc
    # Numpy solution with comments
    # Set up array with trig functions with rotation angle arg
    trig_array = np.array([[np.cos(rz), -np.sin(rz)], [np.sin(rz), np.cos(rz)]])
    print('trig_array')
    print(trig_array)
    print('local_point_array')
    # Set up array with local points
    local_point_array = np.array([xp, yp])
    print(local_point_array)
    print('center_point_array')
    # Set up array with center coords
    center_point_array = np.array([xc, yc])
    print(center_point_array)
    # Perform array multiplication
    print('trig_array * local_point_array')
    print(trig_array * local_point_array)
    product_array = trig_array * local_point_array
    # Transpose array product so that addition works correctly cols must become rows
    print('np.transpose(product_array)')
    print(np.transpose(product_array))
    # Perform array addition
    print('global_point_array = center_point_array + np.transpose(product_array)')
    global_point_array = center_point_array + np.transpose(product_array)
    print(global_point_array)
    # Delete extra row hanging on from addition
    print('1d global_point_array')
    global_point_array = np.delete(global_point_array, 1, axis=0)
    print(global_point_array)

    # Compare to non-Numpy Python arithmetic solution
    c11 = np.cos(rz)
    print('C11', c11)
    c12 = -np.sin(rz)
    print('c12', c12)
    c21 = np.sin(rz)
    print('c21', c21)
    c22 = np.cos(rz)
    print('c22', c22)
    xpp = xp * c11 + yp * c12  # —-xpp,ypp=rotated coordinates relative to xc,yc
    print('xpp', xpp)
    ypp = xp * c21 + yp * c22
    print('ypp', ypp)
    xg = xc + xpp  # —-xg,yg=rotated coordinates relative to xg,yg
    yg = yc + ypp
    print('xg', xg)
    print('yg', yg)

    print('-----')

    return [global_point_array[0][0], global_point_array[0][1]]

def rotz(xc, yc, xp, yp, rz):  # ——–xp,yp=un-rotated coordinates relative to xc,yc

    c11 = np.cos(rz)
    print('C11', c11)
    c12 = -np.sin(rz)
    print('c12', c12)
    c21 = np.sin(rz)
    print('c21', c21)
    c22 = np.cos(rz)
    print('c22', c22)
    xpp = xp * c11 + yp * c12  # —-xpp,ypp=rotated coordinates relative to xc,yc
    print('xpp', xpp)
    ypp = xp * c21 + yp * c22
    print('ypp', ypp)
    xg = xc + xpp  # —-xg,yg=rotated coordinates relative to xg,yg
    yg = yc + ypp
    print('xg', xg)
    print('yg', yg)
    return [xg, yg]


def rotation():
    plt.axis([-10, 140, 90, -10])
    plt.axis('on')
    plt.grid(True)

    # PLOT AXES
    plt.arrow(0, 0, 40, 0, head_length=4, head_width=2, color='b')
    plt.arrow(0, 0, 0, 40, head_length=4, head_width=2, color='b')

    xc = 40
    yc = 10

    plt.plot([xc - 30, xc + 90], [yc, yc], linewidth=1, color='k')  # —-X
    plt.plot([xc, xc], [yc - 5, yc + 75], linewidth=1, color='k')  # —-Y

    plt.text(30, -2, 'Xg', color='b')
    plt.text(-7, 33, 'Yg', color='b')
    plt.scatter(xc, yc, s=20, color='k')
    plt.text(xc + 3, yc - 2, '(xc,yc)')


    # Coordinates of first Point 1 relative to xc,yc
    xp = 60
    yp = 0

    # PLOT POINT 1
    rz = 0
    rz = rz * np.pi / 180
    [xg, yg] = np_rotz(xc, yc, xp, yp, rz)
    plt.scatter(xg, yg, s=30, color='k')
    plt.text(xg + 1, yg + 6, 'P1', color='k')


    # PLOT POINT 2
    rz = 30
    rz = rz * np.pi / 180
    xg, yg = np_rotz(xc, yc, xp, yp, rz)
    plt.scatter(xg, yg, s=30, color='grey')
    plt.text(xg + 1, yg + 6, 'P2', color='grey')


    # PLOT POINT 3
    rz = 60
    rz = rz * np.pi / 180
    [xg, yg] = np_rotz(xc, yc, xp, yp, rz)
    plt.scatter(xg, yg, s=30, color='r')
    plt.text(xg + 1, yg + 6, 'P3', color='r')
    xpp3 = xg  # ——save for later in line 76
    ypp3 = yg


    # PLOT POINT 4
    rz = 90
    rz = rz * np.pi / 180
    [xg, yg] = np_rotz(xc, yc, xp, yp, rz)  # was [xg,yg]=rotz(xp1,yp1,rz)
    plt.scatter(xg, yg, s=30, color='grey')
    plt.text(xg + 1, yg + 6, 'P4', color='grey')  # plt.text(xp2+1,yp2+6,'P4',color='grey')


    # PLOT VECTORS TO POINTS
    plt.arrow(0, 0, xc - 4, yc - 1, head_length=4, head_width=2, color='k')
    plt.text(28, 6, r'$\mathbf{C}$', color='k')

    plt.arrow(0, 0, xpp3 - 3, ypp3 - 3, head_length=4, head_width=2, color='b')
    plt.text(45, 50, r'$\mathbf{Pg}$', color='b')
    plt.arrow(xc, yc, xpp3 - 2 - xc, ypp3 - 5 - yc, head_length=4, head_width=2, color='r')
    plt.text(61, 40, r'$\mathbf{P^{\prime}}$', color='r')

    plt.arrow(xc, yc, xp - 4, yp, head_length=4, head_width=2, color='k')
    plt.text(80, yc - 2, r'$\mathbf{P}$', color='k')

    plt.show()
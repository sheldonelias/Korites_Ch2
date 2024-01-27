import math

import matplotlib.pyplot as plt
import numpy as np

def vector():
    plt.axis([-20, 130, 80, -20])

    plt.axis('on')
    plt.grid(True)

    # Green line drawn with high frequency dots set to .5. Low number makes more dots
    x1 = 20
    x2 = 120
    y1 = 40
    y2 = 20

    dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # print(dist)
    # print(math.ceil(dist) * 2)
    ux = (x2 - x1) / dist
    uy = (y2 - y1) / dist

    count = 0
    for l in np.arange(0, dist, .5): # <-- frequency set to .5
        count += 1
        # print(count)
        px = x1 + l * ux
        py = y1 + l * uy
        plt.scatter(px, py, s=1, color='g')

    # Blue line drawn with low frequency dots set to 2
    x1 = 17
    x2 = 123
    y1 = 4
    y2 = 66

    q = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ux = (x2 - x1) / q
    uy = (y2 - y1) / q

    count = 0
    for l in np.arange(0, q, 2): # << frequency set to 2 here
        px = x1 + l * ux
        py = y1 + l * uy
        plt.scatter(px, py, s=1, color='b')
        count += 1

    print('(q-0)/2:', (q-0)/2)
    print('count:', count)

    # Purple line drawn with plot()
    x1 = 20
    x2 = 120
    y1 = 45
    y2 = 25

    q = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ux = (x2 - x1) / q
    uy = (y2 - y1) / q

    x_start = -1
    y_start = -1
    x_end = -1
    y_end = -1

    counter = 0
    for l in np.arange(0, q, 2):
        print(l)
        px = x1 + l * ux
        py = y1 + l * uy
        print(px, py)
        if counter == 0:
            x_start = px
            y_start = py -10
        else:
            x_end = px
            y_end = py -10
        counter =+ 1



    plt.plot([x_start, x_end], [y_start, y_end], color='purple')

    plt.show()

vector()
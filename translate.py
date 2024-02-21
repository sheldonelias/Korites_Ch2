import numpy as np
import matplotlib.pyplot as plt

def translate():

    # translate_triangle_horizontal_List_comprehension()
    # triangle_static()
    # translate_triangle_by_addition_statements()
    # translate_triangle_by_list_comprehension()
    # translate_box_by_nparray_addition()
    # translate_box_by_nparray_dxscalar()
    # translate_diagonal_box()
    pass

def triangle_static():

    x1=-10
    x2=140
    y1=90
    y2=-10
    plt.axis([x1,x2,y1,y2])

    plt.axis('on')
    plt.grid(True)


    plt.title('Static Triangle')

    #--- draw triangle

    x_vertices=[20,30,40,20]
    y_vertices=[40,20,40,40]
    plt.plot(x_vertices,y_vertices,color='k')
    plt.plot(x_vertices,y_vertices,color='k')
    plt.plot(x_vertices,y_vertices,color='k')

    plt.show()

    #————————————————————————————additive translate triangle


def translate_triangle_by_addition():
    x1 = -10
    x2 = 140
    y1 = 90
    y2 = -10
    plt.axis([x1, x2, y1, y2])

    plt.axis('on')
    plt.grid(True)

    plt.title('Translation by Varied Addition')

    # --- draw triangle

    x_vertices = [20, 30, 40, 20]
    y_vertices = [40, 20, 40, 40]
    plt.plot(x_vertices, y_vertices, color='k')
    plt.plot(x_vertices, y_vertices, color='k')
    plt.plot(x_vertices, y_vertices, color='k')

    # Various dx vals
    dx1 = 10
    dx2 = 15
    dx3 = 25
    dx4 = 40
    print('x_vertices', x_vertices)
    # Use list comprehension technique
    x_vertices = [dx1 + val for val in x_vertices]
    print('x_vertices after translation', x_vertices)
    plt.plot(x_vertices,y_vertices,color='g')
    x_vertices = [dx2 + val for val in x_vertices]
    print('x_vertices after translation', x_vertices)
    plt.plot(x_vertices,y_vertices,color='g')
    x_vertices = [dx3 + val for val in x_vertices]
    print('x_vertices after translation', x_vertices)
    plt.plot(x_vertices,y_vertices,color='g')
    x_vertices = [dx4 + val for val in x_vertices]
    print('x_vertices after translation', x_vertices)
    plt.plot(x_vertices,y_vertices,color='g')


    print('y_vertices', y_vertices)
    # Use list comprehension technique
    y_vertices = [dx1 + val for val in y_vertices]
    print('x_vertices after translation', y_vertices)
    plt.plot(x_vertices, y_vertices, color='b')
    y_vertices = [dx2 + val for val in y_vertices]
    print('y_vertices after translation', y_vertices)
    plt.plot(x_vertices, y_vertices, color='b')
    y_vertices = [dx3 + val for val in y_vertices]
    print('x_vertices after translation', x_vertices)
    plt.plot(x_vertices, y_vertices, color='b')
    y_vertices = [dx4 + val for val in x_vertices]
    print('x_vertices after translation', x_vertices)
    plt.plot(x_vertices, y_vertices, color='b')

    plt.show()



def box_translation():

    edge_length = 5
    xc_start = 0
    yc_start = 20
    xc_end = 50
    yc_end = 20
    dx = 10

    x1 = xc_start - 10
    x2 = xc_end + 10
    y1 = yc_start - 10
    y2 = yc_end + 10
    #plt.axis([x1, x2, y1, y2])

    plt.axis('on')
    plt.grid(True)

    for x_val in np.arange(0, xc_end, dx):
        x_vertices = [x_val, x_val , x_val + edge_length, x_val + edge_length, x_val ]
        y_vertices = [yc_start - x_val, yc_start - edge_length - x_val, yc_start - edge_length - x_val, \
                      yc_start - x_val, yc_start - x_val]

        print('x_vals:', x_vertices)
        print('y_vals:', y_vertices)
        plt.plot(x_vertices, y_vertices, 'b')


    plt.show()
    
    '''
    '''
    # ————————————————————————————————————————————translate box
    '''
    '''
def translate_box_by_nparray_addition():
    print('--- NP Array Translation 1---')
    x1 = -10
    x2 = 140
    y1 = 90
    y2 = -10
    plt.axis([x1, x2, y1, y2])

    plt.axis('on')
    plt.grid(True)

    dx = 15
    y_vals = [40, 30, 30, 40, 40]
    x_vals = [0, 0, 10, 10, 0]

    x_vals_arr = np.array(x_vals)

    for moves in range(10):
        print('x_vals_arr:', x_vals_arr)
        x_vals_arr += dx
        plt.plot(x_vals_arr, y_vals, 'b')
        print(x_vals_arr[len(x_vals_arr)-1], y_vals[len(y_vals)-1])

    plt.show()

def translate_box_by_nparray_dxscalar():
      
    print('--- NP Array Translation 2---')

    figures, axes = plt.subplots()
    axes.set_aspect(1)
    x1 = -10
    x2 = 150
    y1 = -10
    y2 = 100
    plt.axis([x1, x2, y1, y2])
    plt.title('Translation by Scaling')

    plt.axis('on')
    plt.grid(True)

    dx = 6
    dy = 2
    y_vals = [55, 50, 50, 55, 55]
    x_vals = [0, 0, 5, 5, 0]

    x_vals_arr = np.array(x_vals)
    y_vals_arr = np.array(y_vals)

    print(x_vals_arr)

    for scalar in range(10):
        x_vals_arr += scalar * dx
        y_vals_arr += scalar * dy
        print('x_vals_arr:', x_vals_arr)
        plt.plot(x_vals_arr, y_vals_arr, 'b')

    plt.show()


def translate_triangle_by_list_comprehension():
    x1 = -10
    x2 = 140
    y1 = 90
    y2 = -10
    plt.axis([x1, x2, y1, y2])

    plt.axis('on')
    plt.grid(True)

    x_vertices = [20, 30, 40, 20]
    y_vertices = [40, 20, 40, 40]
    plt.plot(x_vertices, y_vertices, color='k')
    plt.plot(x_vertices, y_vertices, color='k')
    plt.plot(x_vertices, y_vertices, color='k')

    dx = 10

    for count in range(0, 100, 10):
        x_vertices = [x_val + dx for x_val in x_vertices]
        print('x_vals:', x_vertices)
        print('y_vals:', y_vertices)
        plt.plot(x_vertices, y_vertices, 'k')

    plt.show()
    pass


def translate_triangle_horizontal_List_comprehension():
    figure, axes = plt.subplots()
    axes.set_aspect(1)

    x1 = -10
    x2 = 140
    y1 = 90
    y2 = -10
    plt.axis([x1, x2, y1, y2])

    plt.axis('on')
    plt.grid(True)

    x_vertices = [20, 30, 40, 20]
    y_vertices = [40, 20, 40, 40]
    plt.plot(x_vertices, y_vertices, color='k')
    plt.plot(x_vertices, y_vertices, color='k')
    plt.plot(x_vertices, y_vertices, color='k')

    dx = 10

    for count in range(0, 100, dx):
        x_vertices = [x_val + dx for x_val in x_vertices]

        print('x_vertices:', x_vertices)

        plt.plot(x_vertices, y_vertices, 'k')

    plt.show()

'''
Quiz 2 Review | Problem 7
'''

def translate_diagonal_box_quiz2_review():
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    box_edge_length = 5
    xc_start = 0
    xc_end = 50
    yc_start = 20
    yc_end = 50
    dx = 10

    x1 = xc_start - 10
    x2 = xc_end + 10
    y1 = -range(xc_end)[-1] - 10
    y2 = yc_end + 10
    plt.axis([x1, x2, y1, y2])

    plt.axis('on')
    plt.grid(True)

    for x_val in np.arange(0, xc_end, dx):
        x_vertices = [x_val, x_val, x_val + box_edge_length, x_val + \
                      box_edge_length, x_val]

        ''' 
        # Code before solution
        y_vertices = [yc_start, yc_start - box_edge_length, yc_start - \
                      box_edge_length, yc_start, yc_start]
        '''

        y_vertices = [yc_start - x_val, yc_start - box_edge_length - x_val, \
                      yc_start - box_edge_length - x_val, yc_start - x_val, \
                      yc_start - x_val]

        print('x_vals:', x_vertices)
        print('y_vals:', y_vertices)
        plt.plot(x_vertices, y_vertices, 'b')

    plt.show()

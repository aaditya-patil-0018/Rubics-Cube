import numpy as np

#----------------------------------------------------------------------------------------------------------------------------------------------------

class Sides:
    bottom = 0
    top = 1
    front = 2
    back = 3
    left = 4
    right = 5

#----------------------------------------------------------------------------------------------------------------------------------------------------

cube = np.empty(shape=(6, 3, 3), dtype='str')

#----------------------------------------------------------------------------------------------------------------------------------------------------

cube[Sides.bottom, :, :] = 'w'
cube[Sides.top, :, :] = 'y'
cube[Sides.front, :, :] = 'b'
cube[Sides.back, :, :] = 'g'
cube[Sides.left, :, :] = 'm'
cube[Sides.right, :, :] = 'r'

#cube[Sides.right, 0, 2] = 'k'

#----------------------------------------------------------------------------------------------------------------------------------------------------
def debug():
    # top
    for y in range(2, -1, -1):
        line = "   "
        for x in range(0, 3):
            line += cube[Sides.top, x, y]
        print(line)

    # left, front, right, back
    for y in range(2, -1, -1):
        line = ""
        for side in [Sides.left, Sides.front, Sides.right, Sides.back]:
            for x in range(0, 3):
                line += cube[side, x, y]
        print(line)

    # bottom
    for y in range(2, -1, -1):
        line = "   "
        for x in range(0, 3):
            line += cube[Sides.bottom, x, y]
        print(line)
#----------------------------------------------------------------------------------------------------------------------------------------------------

def right():
    tmp = np.array(cube[Sides.front, 2, :])
    cube[Sides.front, 2, :] = cube[Sides.bottom, 0, :]
    cube[Sides.bottom, 0, :] = cube[Sides.back, 0, :]
    cube[Sides.back, 0, :] = cube[Sides.top, 2, :]
    cube[Sides.top, 2, :] = tmp
    '''print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Top')
    print(cube[Sides.top,:,:])
    print('-'*20)
    print('Bottom')
    print(cube[Sides.bottom,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)'''
    cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :], -1)
    return "R"
#right()

def right_counter():
    tmp = np.array(cube[Sides.front, 2, :])
    cube[Sides.front, 2, :] = cube[Sides.top, 2, :]
    cube[Sides.top, 2, :] = cube[Sides.back, 0, :]
    cube[Sides.back, 0, :] = cube[Sides.bottom, 0, :]
    cube[Sides.bottom, 0, :] = tmp
    '''print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Top')
    print(cube[Sides.top,:,:])
    print('-'*20)
    print('Bottom')
    print(cube[Sides.bottom,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)'''
    cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :])
    return "R'"
#right_counter()

#-------------------------------------------------------------------------------------------------------------------------------------------------

def left():
    tmp = np.array(cube[Sides.front, 0, :])
    cube[Sides.front, 0, :] = cube[Sides.top, 0, :]
    cube[Sides.top, 0, :] = cube[Sides.back, 2, :]
    cube[Sides.back, 2, :] = cube[Sides.bottom, 2, :]
    cube[Sides.bottom, 2, :] = tmp
   
   '''
    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Top')
    print(cube[Sides.top,:,:])
    print('-'*20)
    print('Bottom')
    print(cube[Sides.bottom,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    '''

    cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :])
    return "L"

#left()

def left_counter():
    tmp = np.array(cube[Sides.front, 0, :])
    cube[Sides.front, 0, :] = cube[Sides.bottom, 2, :]
    cube[Sides.bottom, 2, :] = cube[Sides.back, 2, :]
    cube[Sides.back, 2, :] = cube[Sides.top, 0, :]
    cube[Sides.top, 0, :] = tmp
    
    '''
    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Top')
    print(cube[Sides.top,:,:])
    print('-'*20)
    print('Bottom')
    print(cube[Sides.bottom,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    '''

    cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :], -1)
    return "L'"

#left_counter()

#--------------------------------------------------------------------------------------------------------------------------------------------------

def up():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 2] = cube[Sides.right, :, 2]
    cube[Sides.right, :, 2] = cube[Sides.back, :, 2]
    cube[Sides.back, :, 2] = cube[Sides.left, :, 2]
    cube[Sides.left, :, 0] = tmp

    cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :], -1)
    return "U"


def up_counter():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 2] = cube[Sides.left, :, 2]
    cube[Sides.left, :, 2] = cube[Sides.back, :, 2]
    cube[Sides.back, :, 2] = cube[Sides.right, :, 2]
    cube[Sides.right, :, 0] = tmp

    cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :])
    return "U'"

#----------------------------------------------------------------------------------------------------------------------------------------------------

def down():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 0] = cube[Sides.left, :, 0]
    cube[Sides.left, :, 0] = cube[Sides.back, :, 0]
    cube[Sides.back, :, 0] = cube[Sides.right, :, 0]
    cube[Sides.right, :, 0] = tmp

    cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :], -1)
    return "D"


def down_counter():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 0] = cube[Sides.right, :, 0]
    cube[Sides.right, :, 0] = cube[Sides.back, :, 0]
    cube[Sides.back, :, 0] = cube[Sides.left, :, 0]
    cube[Sides.left, :, 0] = tmp

    cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :])
    return "D'"

#----------------------------------------------------------------------------------------------------------------------------------------------------

def front():
    tmp = np.array(cube[Sides.top, :, 0])
    cube[Sides.top, :, 0] = cube[Sides.left, 0, :]
    cube[Sides.left, 0, :] = cube[Sides.bottom, :, 0]
    cube[Sides.bottom, :, 0] = cube[Sides.right, 0, :]
    cube[Sides.right, 0, :] = tmp

    cube[Sides.front, :, :] = np.rot90(cube[Sides.front, :, :], -1)
    return "F"


def front_counter():
    for number in range(3):
        front()
    return "F'"

#----------------------------------------------------------------------------------------------------------------------------------------------------

def back():
    for number in range(3):
        back_counter()
    return "B"


def back_counter():
    tmp = np.array(cube[Sides.top, :, 2])
    cube[Sides.top, :, 2] = cube[Sides.left, 2, :]
    cube[Sides.left, 2, :] = cube[Sides.bottom, :, 2]
    cube[Sides.bottom, :, 2] = cube[Sides.right, 2, :]
    cube[Sides.right, 2, :] = tmp

    cube[Sides.back, :, :] = np.rot90(cube[Sides.back, :, :], -1)
    return "B'"

#-----------------------------------------------------------------------------------------------------------------------------------------------------

method_list = [right, right_counter, left, left_counter, up, up_counter, down, down_counter]

#-----------------------------------------------------------------------------------------------------------------------------------------------------

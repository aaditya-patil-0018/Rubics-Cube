import numpy as np

class Sides:
    bottom = 0
    top = 1
    front = 2
    back = 3
    left = 4
    right = 5

cube = np.empty(shape=(6, 3, 3), dtype='str')

cube[Sides.bottom, :, :] = 'w'
cube[Sides.top, :, :] = 'y'
cube[Sides.front, :, :] = 'b'
cube[Sides.back, :, :] = 'g'
cube[Sides.left, :, :] = 'm'
cube[Sides.right, :, :] = 'r'

print('Bottom')
print(cube[Sides.bottom, :, :])
print('-'*20)
print('Top')
print(cube[Sides.top, :, :])
print('-'*20)
print('Front')
print(cube[Sides.front, :, :])
print('-'*20)
print('Back')
print(cube[Sides.back, :, :])
print('-'*20)
print('Left')
print(cube[Sides.left, :, :])
print('-'*20)
print('Right')
print(cube[Sides.right, :, :])
print('-'*20)
print('-'*20)

'''
def down_counter():
    
    tmp = np.array(cube[Sides.front, :, 2])
    cube[Sides.front, :, 2] = cube[Sides.right, :, 2]
    cube[Sides.right, :, 2] = cube[Sides.back, :, 2]
    cube[Sides.back, :, 2] = cube[Sides.left, :, 2]
    cube[Sides.left, :, 2] = tmp
    
    tmp = np.array(cube[Sides.front, :, 2])
    cube[Sides.front, :,2] = cube[Sides.left, :, 2]
    cube[Sides.left, :, 2] = cube[Sides.back, :, 2]
    cube[Sides.back, :, 2] = cube[Sides.right, :, 2]
    cube[Sides.right, :, 2] = tmp
    

    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    print('Right')
    print(cube[Sides.right,:,:])
    print('-'*20)


    #cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :], -1)

    cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :])
    return "D'"

down_counter()
'''

'''
def down():
    #tmp = np.array(cube[Sides.front, :, 2])
    #cube[Sides.front, :, 2] = cube[Sides.right, :, 2]
    #cube[Sides.right, :, 2] = cube[Sides.back, :, 2]
    #cube[Sides.back, :, 2] = cube[Sides.left, :, 2]
    #cube[Sides.left, :, 2] = tmp
    tmp = np.array(cube[Sides.front, :, 2])
    cube[Sides.front, :, 2] = cube[Sides.left, :, 2]
    cube[Sides.left, :, 2] = cube[Sides.back, :, 2]
    cube[Sides.back, :, 2] = cube[Sides.right, :, 2]
    cube[Sides.right, :, 2] = tmp

    cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :], -1)

    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    print('Right')
    print(cube[Sides.right,:,:])
    print('-'*20)

    #cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :])
    return "D"

down()
''
'''
def up_counter():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 0] = cube[Sides.right, :, 0]
    cube[Sides.right, :, 0] = cube[Sides.back, :, 0]
    cube[Sides.back, :, 0] = cube[Sides.left, :, 0]
    cube[Sides.left, :, 0] = tmp

    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    print('Right')
    print(cube[Sides.right,:,:])
    print('-'*20)

    cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :], -1)
    return "U'"

up_counter()
'''
'''
def up():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 0] = cube[Sides.left, :, 0]
    cube[Sides.left, :, 0] = cube[Sides.back, :, 0]
    cube[Sides.back, :, 0] = cube[Sides.right, :, 0]
    cube[Sides.right, :, 0] = tmp

    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    print('Right')
    print(cube[Sides.right,:,:])
    print('-'*20)

    cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :])
    return "U"

up()
'''

'''
def left_counter():
    tmp = np.array(cube[Sides.front, 0, :])
    cube[Sides.front, 0, :] = cube[Sides.bottom, 2, :]
    cube[Sides.bottom, 2, :] = cube[Sides.back, 2, :]
    cube[Sides.back, 2, :] = cube[Sides.top, 0, :]
    cube[Sides.top, 0, :] = tmp

    
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
    

    cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :], -1)
    return "L'"

left_counter()
'''

'''
def left():
    tmp = np.array(cube[Sides.front, 0, :])
    cube[Sides.front, 0, :] = cube[Sides.top, 0, :]
    cube[Sides.top, 0, :] = cube[Sides.back, 2, :]
    cube[Sides.back, 2, :] = cube[Sides.bottom, 2, :]
    cube[Sides.bottom, 2, :] = tmp
   
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

    cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :])
    return "L"

left()
'''
'''
def right_counter():
    tmp = np.array(cube[Sides.front, 2, :])
    cube[Sides.front, 2, :] = cube[Sides.top, 2, :]
    cube[Sides.top, 2, :] = cube[Sides.back, 0, :]
    cube[Sides.back, 0, :] = cube[Sides.bottom, 0, :]
    cube[Sides.bottom, 0, :] = tmp
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
    cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :])
    return "R'"
right_counter()
'''
'''
def right():
    tmp = np.array(cube[Sides.front, 2, :])
    cube[Sides.front, 2, :] = cube[Sides.bottom, 0, :]
    cube[Sides.bottom, 0, :] = cube[Sides.back, 0, :]
    cube[Sides.back, 0, :] = cube[Sides.top, 2, :]
    cube[Sides.top, 2, :] = tmp
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
    cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :], -1)
    return "R"
right()
'''



'''
def right():
    tmp = np.array(cube[Sides.front, 2, :])
    print('TMP =========== ', tmp) 
    print(cube[1,2,:])

    print(cube[Sides.front, 2, :])
    cube[Sides.front, 2, :] = cube[Sides.bottom, 0, :]
    print(cube[Sides.front, 2, :])
    print('Front')
    print(cube[Sides.front, :, :])
    print('-'*20)

    print(cube[Sides.bottom, 2, :])
    print('Bottom')
    print(cube[Sides.bottom, :, :])
    cube[Sides.bottom, 0, :] = cube[Sides.back, 0, :]
    print(cube[Sides.bottom, 2, :])
    print('Bottom')
    print(cube[Sides.bottom, :, :])
    print('-'*20)

    print(cube[Sides.back, 0, :])
    cube[Sides.back, 0, :] = cube[Sides.top, 2, :]
    print(cube[Sides.back, 0, :])
    print('Back')
    print(cube[Sides.back, :, :])
    print('-'*20)

    print(cube[Sides.top, 2, :])
    cube[Sides.top, 2, :] = tmp
    print(cube[Sides.top, 2, :])
    print('Top')
    print(cube[Sides.top, :, :])
    print('-'*20)

Sides.back, :, 2] = cube[Sides.left, :, 2]
    #cube[Sides.left, :, 2] = tmp

    tmp = np.array(cube[Sides.front, :, 2])
    cube[Sides.front, :, 2] = cube[Sides.left,    print(cube[Sides.right, :, :])
    cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :], -1)
    print(cube[Sides.right, :, :])
    print('Right')
    print(cube[Sides.right, :, :])
    print('-'*20)

    return "R"

right()
print('Right Done!!')

def left():
    print('-'*20)
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
    print('-'*20)
    tmp = np.array(cube[Sides.front, 0, :])
    cube[Sides.front, 0, :] = cube[Sides.top, 0, :]
    cube[Sides.top, 0, :] = cube[Sides.back, 2, :]
    cube[Sides.back, 2, :] = cube[Sides.bottom, 0, :]
    cube[Sides.bottom, 2, :] = tmp
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
    cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :])
    return "L"

left()
'''
'''def left_counter():
    tmp = np.array(cube[Sides.front, 0, :])
    cube[Sides.front, 0, :] = cube[Sides.bottom, 0, :]
    cube[Sides.bottom, 0, :] = np.flip(cube[Sides.back, 2, :])
    cube[Sides.back, 2, :] = np.flip(cube[Sides.top, 0, :])
    cube[Sides.top, 0, :] = tmp

    cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :], -1)
    return "L'"
'''
'''
def up():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 2] = cube[Sides.right, :, 2]
    cube[Sides.right, :, 2] = cube[Sides.back, :, 2]
    cube[Sides.back, :, 2] = cube[Sides.left, :, 2]
    cube[Sides.left, :, 2] = tmp
    
    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Right')
    print(cube[Sides.right,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)

    cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :], -1)
    return "U"

def up_counter():
    tmp = np.array(cube[Sides.front, :, 2])
    cube[Sides.front, :, 2] = cube[Sides.left, :, 2]
    cube[Sides.left, :, 2] = cube[Sides.back, :, 2]
    cube[Sides.back, :, 2] = cube[Sides.right, :, 2]
    cube[Sides.right, :, 2] = tmp
    
    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Right')
    print(cube[Sides.right,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)

    cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :])
    return "U'"

up_counter()
print('uc')
up()
print('u')
'''
'''
def down():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 0] = cube[Sides.left, :, 0]
    cube[Sides.left, :, 0] = cube[Sides.back, :, 0]
    cube[Sides.back, :, 0] = cube[Sides.right, :, 0]
    cube[Sides.right, :, 0] = tmp
    
    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    print('right')
    print(cube[Sides.right,:,:])
    print('-'*20)

    cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :], -1)
    return "D"

down()
print('d1')
'''

'''
def down_counter():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 0] = cube[Sides.right, :, 0]
    cube[Sides.right, :, 0] = cube[Sides.back, :, 0]
    cube[Sides.back, :, 0] = cube[Sides.left, :, 0]
    cube[Sides.left, :, 0] = tmp
    
    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('right')
    print(cube[Sides.right,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    print('left')
    print(cube[Sides.left,:,:])
    print('-'*20)

    cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :])
    return "D'"

down_counter()
print('dc')
def down():
    tmp = np.array(cube[Sides.front, :, 0])
    cube[Sides.front, :, 0] = cube[Sides.left, :, 0]
    cube[Sides.left, :, 0] = cube[Sides.back, :, 0]
    cube[Sides.back, :, 0] = cube[Sides.right, :, 0]
    cube[Sides.right, :, 0] = tmp

    print('Front')
    print(cube[Sides.front,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)
    print('Back')
    print(cube[Sides.back,:,:])
    print('-'*20)
    print('right')
    print(cube[Sides.right,:,:])
    print('-'*20)

    cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :], -1)
    return "D"

down()
print('d')

def front():
    tmp = np.array(cube[Sides.top, :, 0])
    cube[Sides.top, :, 0] = cube[Sides.left, 2, :]
    cube[Sides.left, 2, :] = cube[Sides.bottom, :, 2]
    cube[Sides.bottom, :, 2] = cube[Sides.right, 0, :]
    cube[Sides.right, 0, :] = tmp
    ''' 
    print('Top')
    print(cube[Sides.top,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)
    print('Bottom')
    print(cube[Sides.bottom,:,:])
    print('-'*20)
    print('right')
    print(cube[Sides.right,:,:])
    print('-'*20)
    '''
    cube[Sides.front, :, :] = np.rot90(cube[Sides.front, :, :], -1)
    return "F"
#front()

def front_counter():
    for number in range(3):
        front()
        if number == 2:
            print('Top')
            print(cube[Sides.top,:,:])
            print('-'*20)
            print('Left')
            print(cube[Sides.left,:,:])
            print('-'*20)
            print('Bottom')
            print(cube[Sides.bottom,:,:])
            print('-'*20)
            print('right')
            print(cube[Sides.right,:,:])
            print('-'*20)
    return "F'"
front_counter()
'''
'''
def back_counter():
    tmp = np.array(cube[Sides.top, :, 2])
    cube[Sides.top, :, 2] = cube[Sides.left, 0, :]
    cube[Sides.left, 0, :] = cube[Sides.bottom, :, 0]
    cube[Sides.bottom, :, 0] = cube[Sides.right, 2, :]
    cube[Sides.right, 2, :] = tmp
    
    print('Top')
    print(cube[Sides.top,:,:])
    print('-'*20)
    print('Left')
    print(cube[Sides.left,:,:])
    print('-'*20)
    print('Bottom')
    print(cube[Sides.bottom,:,:])
    print('-'*20)
    print('right')
    print(cube[Sides.right,:,:])
    print('-'*20)

    cube[Sides.back, :, :] = np.rot90(cube[Sides.back, :, :], -1)
    return "B'"
back_counter()
'''

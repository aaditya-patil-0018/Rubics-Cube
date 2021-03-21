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

    print(cube[Sides.right, :, :])
    cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :], -1)
    print(cube[Sides.right, :, :])
    print('Right')
    print(cube[Sides.right, :, :])
    print('-'*20)

    return "R"

right()'''
'''
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
up()

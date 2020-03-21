import numpy as np
from PygameUtil import strip_array


test = np.array([[0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,1,1,1,1,0,0,0],
                 [0,0,0,1,1,1,1,0,0,0],
                 [0,0,0,1,1,1,1,0,0,0],
                 [0,0,0,1,1,1,1,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0]])

print(test)

test = strip_array(test)

print(test)

test1 = np.zeros((test.shape[0]+10, test.shape[1]+10))

print(test1)

test1[5:-5,5:-5] = test

print(test1)
import numpy as np
from PygameUtil import strip_array


test = np.array([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,2,2,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])

print(test)

test = strip_array(test)

print(test)
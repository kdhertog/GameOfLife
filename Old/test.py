import numpy as np 

line1 = np.array([0,1])
line2 = np.array([0,0,1])
line3 = np.array([1,1,1,1,0,0,0,0])
new_cell = [line1,line2,line3]

longest = 0
for line in new_cell:
    if len(line) > longest:
        longest = len(line)



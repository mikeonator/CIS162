"""A. Use Numpy to create a 3 by 3 array.  The array will contain the data 241, 33, 41  -  444, 22, 10  -  342, 122, 315.   

B. Add the code to print out the data values in the array. 

C. Add the code to print out the data at location row 1 - column 2 in the array. 

D. Add the code to print the sum of the third column of the array."""

import numpy as np

mikesarray = np.array([[241, 33, 41], [444, 22, 10], [342, 122, 315]])

print(mikesarray)

print(mikesarray[0, 1])

print(mikesarray[0, 2] + mikesarray[1, 2] + mikesarray[2, 2])

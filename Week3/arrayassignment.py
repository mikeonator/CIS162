# Week 3 CIS162 Michael Audi Array Assignment

import numpy as np

# generate array of 25 random integers between 0 and 99 in a 5x5 array
mikearray = np.random.randint(0, 100, (5, 5), dtype=int)

# print entire array
print(mikearray)

# print [2nd row, 3rd column]
print(mikearray[1, 2])

# print sum of all the elements in the array
print(np.sum(mikearray))

# print mean of each row in array
print(np.mean(mikearray, axis=1))

# print maximum value in each column of the array
print(np.max(mikearray, axis=0))

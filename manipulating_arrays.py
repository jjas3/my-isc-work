#interrogation and manipulation of arrays

import numpy as np

# array interrogation
a=range(4)
b= range(10,14)

arr=np.array([a,b])
print arr

    #print the shape in two ways
print arr.shape
print np.shape(arr)

    #print the size in two ways
print arr.size
print np.size(arr)

    #print the max/min in two ways
print arr.max()
print arr.min()
print np.max(arr)
print np.min(arr)

# Modifying the array

print np.reshape(arr, (2,2,2))
print np.transpose(arr)
print np.ravel(arr)
print arr.astype(np.float64)

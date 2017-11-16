#Creating a numpy array from list
import numpy as np
x=[1,2,3,4,5,6,7,8,9,10]
a1=np.array(x, np.int32)
a2=np.array(x, np.float32)

print a1.dtype
print a2.dtype

#creating an array a different way

b1=np.zeros((2,3,4))
print b1
b2=np.ones((3,5,9))
print b2
b3=np.arange(1000)
#print b3

#indexing and slicing arrays

l=[2,3.5,5,6,9,100,-4]
l1D=np.array(l)
print l1D[1] #3.5
print l1D[1:4] #3.5,5.,6.

l2=[[2,3.5,5,6,9,100,-4],[8,9,6,-3,5.6,44,-1],[3,4,5,6,7,8,9]]
l2D=np.array(l2)
print l2D
print l2D[:,3] # every row, column 4 
print l2D[1:4, 0:4] # rows 2-4, column 1-4
print l2D[1:,2] #rows 2-end, column 3

# Working with missing values (masks)

import numpy as np
import numpy.ma as MA

    # creating a masked array

# creating a masked array from a list of values. (fill_value is what is there when there is no data or it is removed - it is optional)

marr = MA.masked_array(range(10), fill_value=-999)
print marr, marr.fill_value

marr[2]=MA.masked #removes the third element
print marr # marr now contains nothing at the third element

print marr.mask # shows the boolean array of the mask (third element is the only true)


narr = MA.masked_where(marr>7, marr) #new array
print narr

x = narr.fill_value #finding the fill value of narr, not specified therefore default
print x

print type(x) #type of x is currently numpy.int64

    # creating a mask that is smaller than the array

m1 = MA.masked_array(range(1,9)) # new array, no fill value specified
print m1
m2=m1.reshape(2,4) #reshaping the m1 array into a 2,4 array
print m2

m3= MA.masked_greater(m2,6) #a slightly different way of masking to what we saw above - perhaps easier to understand? 

print m3

print m3*100

m4 = m3 - np.ones((2,4)) #takes an array of ones away (interestingly becomes an array of floats)

print m4

print type(m4) #masked array



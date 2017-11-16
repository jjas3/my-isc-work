# Array calculations and operations

import numpy as np

    # Array calculations

#a = np.array([range(4), range(10,14)])
#b = np.array([2,-1,1,0])

#c= a * b
#print c

#d = b * 100
#print d

#e = b * 100.0
#print e

#print d == e

    # Array comparisons

#arr = np.array([range(10)])
#print arr

        #two ways of expressing the condition less than 3

#print arr < 3
#print np.less(arr,3)

        # setting a condition
#condition = np.logical_or(arr < 3, arr > 8)
        # using the condition in a where 
#new_arr = np.where(condition, arr*-5, arr*5)
#print new_arr

    # Mathematical functions that work on arrays

        #a function that writes a 2D array of horizontal zonal (E-W) wind components (u, in m/s) and a 2D array of horizontal meridional (S-N) wind components (v, in m/s) and returns an array of the total wind magnitude

def calc_wind_magnitude (u,v,min_mag = 0.1):
    mag = ((u**2)+(v**2))**0.5
    output= np.where(mag>min_mag, mag, min_mag)
    return output
       
       # using the function

u = np.array([[4,5,0.00005],[2,3,4]])
v = np.array([[2,2,0.009],[4,4,4]])

print calc_wind_magnitude(u,v)

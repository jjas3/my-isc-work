mylist = [23, "hi", 2.4e-10]
for (i,name) in enumerate(mylist):
    print i, name
    
first, middle, last = mylist
print( first, middle, last)
first, middle, last = middle, last, first
print( first, middle, last)

import netCDF4
dataset = netCDF4.Dataset("/home/user01/ncas-isc/python/exercises/example_data/ggas2014121200_00-18.nc")


#helpful vairable to print and split the output up into chunks

a=("Page Break")

#loop over the variables in the dataset and print their names
for var in dataset.variables:
     print var

# set the NCDF variable SSTK to the python variable sst
sst = dataset.variables['SSTK']
print sst

print a

#loop over the dimensions of sst and print out the name and length
for l in sst.dimensions:
     print l, len(dataset.variables[l])

print a

#print the size and shape of sst
print sst.shape, sst.size

print a 

#loop over the NetCDF attributes of sst and print them 
for attr in sst.ncattrs():
    print attr, '=', getattr(sst,attr)


#take a slice of sst and assign it to arr
arr = sst[1,0,10:20,30:35]

#find out the tyoe of arr
print type(arr)

#assign a list of the sst dims
dims=sst.dimensions
print dims

#assign dictionary of dataset variables
vars=dataset.variables

#extract slices of each dataset variable matching those in arr
arr_time = vars["time"][1]
arr_level = vars["surface"][0]
arr_lats = vars["latitude"][10:20]
arr_lons = vars["longitude"][30:35]

#loop through each new variable and print
for vals in (arr_time, arr_level, arr_lats, arr_lons):
    print vals

#create an empty dictionay and loop through the netCDF variables attributes of sst to cp into dictionary
metadata = {}

for attr in sst.ncattrs():
    metadata[attr] = getattr(sst,attr)

# print dictionary

print metadata

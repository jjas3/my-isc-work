from map_data import *
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#fig = plt.figure()

#m = Basemap(projection = 'cyl', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution ='c')
#m.drawcoastlines()
#im1 = m.pcolormesh(lons,lats,tas,shading='flat', cmap = plt.cm.jet, 
#latlon=True)
#plt.savefig("tas1.png")
#plt.show()

fig = plt.figure()
plt.title('Change in surface air temp from...')
m = Basemap(projection = 'cyl', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution ='c')

m.drawcoastlines()
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

im1 = m.pcolormesh(lons,lats,tas,shading='flat', cmap = plt.cm.jet, 
latlon=True)

cb = m.colorbar(im1,"bottom")

plt.savefig("tas2.png")
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 18:38:43 2014
use http://matplotlib.org/basemap/api/basemap_api.html for reference
@author: matt
"""
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv # output writing
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# lat_ts is the latitude of true scale.
# resolution: ( c (crude), l (low), i (intermediate), h (high), f (full) or None)

## import model domain
coast = np.loadtxt(
'C:\Users\matt\Documents\umd\spring_2014\MEES616\class_20140306\llbounds.csv',
delimiter=',')
start = np.loadtxt(
'C:\Users\matt\Documents\umd\spring_2014\MEES616\class_20140306\para10000002.csv',
delimiter=',')


## Generate linear array
particles = 5000
size = np.floor(np.sqrt(particles)) #calculate the grid size for lat lon
print size
lat = np.linspace(39.48,39.5,size) # generate even grid lat
lon = np.linspace(-76.025,-76.053,size) # generate even grid lon
lati,loni = np.meshgrid(lat,lon) # create the meshgrid
depth = [-0.25] * size**2
start_time = [0] * size**2
habitat_ID_num = [101001] * size**2
print len(depth)
#size(lati.flatten)
## Mapping
# Full Bay
m = Basemap(projection='merc',llcrnrlat=36.5,urcrnrlat=40,\
            llcrnrlon=-77.5,urcrnrlon=-75,lat_ts=20,resolution='i')
# Zoomed to mouth of susque
#m = Basemap(projection='merc',llcrnrlat=39.25,urcrnrlat=39.75,\
#           llcrnrlon=-76.25,urcrnrlon=-75.75,lat_ts=20,resolution='i')
m.drawcoastlines()
#m.shadedrelief()
#m.bluemarble()
#m.etopo()
m.fillcontinents(color='grey',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,.5),labels=[1,0,0,0],fontsize=10)
m.drawmeridians(np.arange(-180.,181.,.5),labels=[0,0,0,1],fontsize=10)
m.scatter(loni.flatten(),lati.flatten(),latlon='True',marker='.',color='b',label="particle locations")

#m.drawmapboundary(fill_color='aqua')

m.plot(coast[:,0],coast[:,1],latlon='True',linewidth=.75,color='r',label="model boundary")#,'k-',markersize=1) # model domain

blat = np.linspace(39.25,39.75,size) # generate even grid lat
upleft = [-76.25,39.75]
upright = [-75.75,39.75]
lowleft = [-76.25,39.25]
lowright = [-75.75,39.25]
blon = np.linspace(-75.75,-76.25,size) # generate even grid lon
boxlat,boxlon = np.meshgrid(blat,blon) # create the meshgrid
#m.plot(upleft,upright,latlon='True',linewidth=2,color='k')
#m.minorticks_on()
#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),loc=3,mode="expand", borderaxespad=0.)
#plt.legend(loc=8)
#plt.title("Initial Particle Locations")
#plt.text(0.5, 0.06, 'Longitude [DD.D]', ha='center', va='center', fontsize=16)
#plt.text(0.05, 0.5, 'Latitude [DD.DD]', ha='center', va='center', fontsize=16, rotation='vertical')
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
plt.savefig("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\\initial_particle_location_map.png", dpi=200)
plt.show()
#ofile = open('Initial_particle_locations.csv','wb') # creates output file
#writer = csv.writer(ofile,delimiter=',') # describes what it will look like
#rows = zip(loni.flatten(), lati.flatten(),depth,start_time,habitat_ID_num) # write all rows at once
#writer.writerows(rows) # write rows
#ofile.close() # close file


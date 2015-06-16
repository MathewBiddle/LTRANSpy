# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 20:18:23 2014

@author: matt
"""

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
import os
import time
#import time
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# lat_ts is the latitude of true scale.
# resolution: ( c (crude), l (low), i (intermediate), h (high), f (full) or None)

tic1 = time.time()
depth = []
code = []
lon = []
lat = []
# load model boundaries
coast = np.loadtxt(
'C:\Users\matt\Documents\umd\spring_2014\MEES616\class_20140306\llbounds.csv',
delimiter=',')

# List directory where your data is
#direct = 'C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07'
#direct = 'C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\silt_test_1997_2014_04_09'
#direct = 'C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\clay_test_1997_2014_04_10'
direct = 'C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1998_2014_04_10'
#direct = 'C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\silt_test_1998_2014_04_12' # DONE
#direct = 'C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\clay_test_1998_2014_04_13'
#parafiles = os.listdir('C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07')
parafiles = os.listdir(direct)
parafiles.remove('endfile.csv') # removes endfile.csv
parafiles.remove('images') # removes images directory

base = os.path.basename(direct)
size, test, year, runyear, runmonth, runday = base.split("_")
#print "%s %s" % (size,year)
#parafiles.remove('llbounds.bln')
count = 0
for i in parafiles:
    tic2 = time.time()
    count = count+1
    filename, ext = i.split(".",1) 
#    filenames = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07\%s" % i
    filenames = "%s\%s" % (direct,i)
    title = "%s %s hour %s" % (size, year, count) # % i # adjust to (os.path.basename(direct), i)
#    savefilename = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07\images\%s.png" % i
    savefilename = "%s\images\%s.png" % (direct,filename)
    print "processing: %s" % filenames
    with open(filenames, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            depth.append(float(row[0]))
            code.append(float(row[1]))
            lon.append(float(row[2]))
            lat.append(float(row[3]))
        #print len(lon)
    print "generating plot: %s" % title
    #print max(code)
## High resolution llcrnrlat=39.25, llcrnrlon=-76.25
    m = Basemap(projection='merc',llcrnrlat=38.0,urcrnrlat=39.75,\
           llcrnrlon=-77,urcrnrlon=-75.75,lat_ts=20,resolution='i')
    m.drawcoastlines()
    m.fillcontinents(color='grey',lake_color='aqua')
    #m.drawmapboundary(fill_color='aqua')
           #draw parallels and meridians.
    m.drawparallels(np.arange(-90.,91.,.25),labels=[1,0,0,0],fontsize=10)
    m.drawmeridians(np.arange(-180.,181.,.5),labels=[0,0,0,1],fontsize=10)
 #   if max(code) == 6:
 #       print 'Alive'
 #       m.scatter(lon,lat,latlon='True',color='blue',marker='.',linewidth=.5,label="particle locations")
 #   else:
 #       print 'Dead'
 #       m.scatter(lon,lat,latlon='True',color='red',marker='.',linewidth=.5,label="particle locations")
    m.scatter(lon,lat,latlon='True',color='blue',marker='.',linewidth=.5,label="particle locations")
    m.plot(coast[:,0],coast[:,1],latlon='True',linewidth=2,color='r',label="model boundary")
    m.drawmapscale(-76.76,38.6,-76.51,39.1,20,barstyle='simple')
    plt.legend(loc=9,fontsize=9)
    plt.title(title)
    #print "saving: %s" % savefilename
    #plt.savefig(savefilename, dpi=100)
    toc2 = time.time()
    print toc2-tic2, 'sec Elapsed'
    #plt.show()
    #time.sleep(15)
    #break
    lon = []
    lat = []
    depth = []
    code = []
    plt.clf()
       #print row
toc1 = time.time()
print toc1-tic1, 'sec Elapsed'
print "Image generation complete!"
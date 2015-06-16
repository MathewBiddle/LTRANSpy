# -*- coding: utf-8 -*-
"""
Created on Mon May 05 15:12:11 2014

@author: matt
"""
import numpy as np
import matplotlib.pyplot as plt
import csv # output writing
#from haversine import haversine
import haversine_mine
import os
from mpl_toolkits.basemap import Basemap

lon_end1 = []
lat_end1 = []
lon_end2 = []
lat_end2 = []

coast = np.loadtxt(
'C:\Users\matt\Documents\umd\spring_2014\MEES616\class_20140306\llbounds.csv',
delimiter=',')
letters = ['A','B','C']
# Get files
# low flow
#path1 = 'C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07\endfile.csv'
#path1 = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\silt_test_1997_2014_04_09\endfile.csv"
path1 = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\clay_test_1997_2014_04_10\endfile.csv"
# high flow
#path2 = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1998_2014_04_10\endfile.csv"
#path2 = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\silt_test_1998_2014_04_12\endfile.csv"
path2 = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\clay_test_1998_2014_04_13\endfile.csv"

#fig, axes = plt.subplots(nrows=1, ncols=3,figsize=(10,10))

with open(path1, 'rb') as f:
                reader = csv.reader(f)
                for row in reader:
                    lat_end1.append(float(row[1]))
                    lon_end1.append(float(row[2]))
with open(path2, 'rb') as f:
                reader = csv.reader(f)
                for row in reader:
                    lat_end2.append(float(row[1]))
                    lon_end2.append(float(row[2]))                    

m = Basemap(projection='merc',llcrnrlat=38.0,urcrnrlat=39.75,\
llcrnrlon=-77,urcrnrlon=-75.75,lat_ts=20,resolution='i')#,ax=axes.flat[0])
m.drawcoastlines()
m.fillcontinents(color='grey',lake_color='aqua')
#m.drawmapboundary(fill_color='aqua')
   #draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,.25),labels=[1,0,0,0],dashes=[2,10],fontsize=10)
m.drawmeridians(np.arange(-180.,181.,.5),labels=[0,0,0,1],dashes=[2,10],fontsize=10)
#m.scatter(north_point_lon,north_point_lat,latlon='True',color='red',marker='o',linewidth=8)
#m.scatter(south_point_lon,south_point_lat,latlon='True',color='red',marker='o',linewidth=8)
m.scatter(lon_end1,lat_end1,latlon='True',color='blue',marker='.',linewidth=.5,\
label="1997 particle locations")
m.scatter(lon_end2,lat_end2,latlon='True',color='green',marker='.',linewidth=.15,\
label="1998 particle locations")
m.plot(coast[:,0],coast[:,1],latlon='True',linewidth=1,color='r',label="model boundary")
m.drawmapscale(-76.76,38.6,-76.51,39.1,20,barstyle='simple')
#axes.flat[0].annotate(letters[0],xy=(0.1, 0.95), xycoords='axes fraction',\
#axes.annotate(letters[0],xy=(0.1, 0.95), xycoords='axes fraction',\
#fontsize=16,xytext=(0.1, .95), textcoords='offset points',ha='left', va='top')
#plt.xlabel('Longitude [DD]')
plt.title('Clay')
plt.text(-77,39.75,0)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 12:42:43 2014

@author: matt
"""
import numpy as np
import matplotlib.pyplot as plt
import csv # output writing
#from haversine import haversine
import haversine_mine
import os
from mpl_toolkits.basemap import Basemap

## Initialize variables
depth_end = []
code_end = []
lon_end = []
lat_end = []
depth_start = []
code_start = []
lon_start = []
lat_start = []
distance = []
paths = []
averages = []
maximums = []
minimums = []
## Get files
# low flow
#path = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07"
#path = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\silt_test_1997_2014_04_09"
#path = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\clay_test_1997_2014_04_10"
# high flow
#path = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1998_2014_04_10"
#path = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\silt_test_1998_2014_04_12"
#path = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\clay_test_1998_2014_04_13"
#parafiles = os.listdir('C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07')
paths.append("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07")
paths.append("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\silt_test_1997_2014_04_09")
paths.append("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\clay_test_1997_2014_04_10")
paths.append("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1998_2014_04_10")
paths.append("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\silt_test_1998_2014_04_12")
paths.append("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\clay_test_1998_2014_04_13")
coast = np.loadtxt(
'C:\Users\matt\Documents\umd\spring_2014\MEES616\class_20140306\llbounds.csv',
delimiter=',')
letters = ['A','C','E','B','D','F']
#fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2)
#fig = plt.figure(figsize=(15,10))
fig, axes = plt.subplots(nrows=2, ncols=3,figsize=(10,10))
## work through each diretory
count = 0
for j in paths:
    #print j
    parafiles = os.listdir(j)
    #print parafiles
## Grab data out of files
    for i in parafiles:
        if i == 'endfile.csv': # last model run
            filenames = "%s\%s" % (j, i)
            #print "processing: %s" % filenames
            with open(filenames, 'rb') as f:
                reader = csv.reader(f)
                for row in reader:
                    code_end.append(float(row[0]))
                    lat_end.append(float(row[1]))
                    lon_end.append(float(row[2]))
                    
        ## Grab min/max for 'spread' claculation
                print 'min'
                #print min(lat_end)
                min_lat_end = min(lat_end)
                #print min_lat_end
                #print lat_end.index(min_lat_end)
                #print type(min_lat_end)
                south_point_lat = lat_end[lat_end.index(min_lat_end)]
                south_point_lon = lon_end[lat_end.index(min_lat_end)]
                #min_lon_end = (x for x in lst if x > 6)
                print 'max'
                #print max(lat_end)
                max_lat_end = max(lat_end)
                #print max_lat_end
                #print lat_end.index(max_lat_end)
                #print lon_end.index(max_lat_end)
                #print type(min_lat_end)
                north_point_lat = lat_end[lat_end.index(max_lat_end)]
                north_point_lon = lon_end[lat_end.index(max_lat_end)]
                #ax1.plot(lat_end,lon_end)
                #plt.show()
                #ind = "ax{0}".format(count)
                #print ind
                #print type(ind)
                #exec("m = Basemap(projection='merc',llcrnrlat=38.0,urcrnrlat=39.75,llcrnrlon=-77,urcrnrlon=-75.75,lat_ts=20,resolution='i',ax=ax%i)",%count)
                m = Basemap(projection='merc',llcrnrlat=38.0,urcrnrlat=39.75,\
           llcrnrlon=-77,urcrnrlon=-75.75,lat_ts=20,resolution='i',ax=axes.flat[count])
                m.drawcoastlines()
                m.fillcontinents(color='grey',lake_color='aqua')
                #m.drawmapboundary(fill_color='aqua')
           #draw parallels and meridians.
                m.drawparallels(np.arange(-90.,91.,.25),labels=[1,0,0,0],fontsize=10)
                m.drawmeridians(np.arange(-180.,181.,.5),labels=[0,0,0,1],fontsize=10)
                #m.scatter(north_point_lon,north_point_lat,latlon='True',color='red',marker='o',linewidth=8)
                #m.scatter(south_point_lon,south_point_lat,latlon='True',color='red',marker='o',linewidth=8)
                m.scatter(lon_end,lat_end,latlon='True',color='blue',marker='.',linewidth=.5,label="particle locations")
                m.plot(coast[:,0],coast[:,1],latlon='True',linewidth=1,color='r',label="model boundary")
                m.drawmapscale(-76.76,38.6,-76.51,39.1,20,barstyle='simple')
                #axes.flat[count].annotate(letters[count],xy=(0.1, 0.95), xycoords='axes fraction',\
                #fontsize=16,xytext=(0.1, .95), textcoords='offset points',ha='left', va='top')
                #plt.xlabel('Longitude [DD]')
                plt.text(-77,39.75,count)
                ## title each plot
                #print os.path.basename(j)
                size, test, year, runyear, runmonth, runday = os.path.basename(j).split("_")
                #print size
                title = "%s %s" % (size, year)
                axes.flat[count].set_title(title) 
                #plt.show()
                count = count+1
                #break
                lat_end=[]
                lon_end=[]
#        elif i == 'para10000002.csv': # first model run
#            #filenames = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07\%s" % i
#            filenames = "%s\%s" % (j, i)
#            #print "processing: %s" % filenames
#            with open(filenames, 'rb') as f:
#                reader = csv.reader(f)
#                for row in reader:
#                    depth_start.append(float(row[0]))
#                    code_start.append(float(row[1]))
#                    lon_start.append(float(row[2]))
#                    lat_start.append(float(row[3]))
### Calculate distances between points, each row is the same particle
#    for k in range(len(lon_start)):
#        distance.append(haversine_mine.distance([lon_start[k],lat_start[k]],[lon_end[k],lat_end[k]]))
#    #print "start:  %f %f" % (lon_start[j],lat_start[j])
#    #print "end:    %f %f" % (lon_end[j],lat_end[j])
#    #print "distance: %f" % distance[j]

## Print statistics
    fig.text(0.5, 0.06, 'Longitude [DD.D]', ha='center', va='center', fontsize=16)
    fig.text(0.05, 0.5, 'Latitude [DD.DD]', ha='center', va='center', fontsize=16, rotation='vertical')
    print "Run: %s" % os.path.basename(j)
#    print "mean: %f km" % np.mean(distance)
#    averages.append(np.mean(distance))
#    print "max: %f km" % max(distance)
#    maximums.append(max(distance))
#    print "min: %f km" % min(distance)
#    minimums.append(min(distance))
#plt.tight_layout()
plt.savefig("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\\final_location_subplot2_no_label.png",dpi=200)
plt.show()
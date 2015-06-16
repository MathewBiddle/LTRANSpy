# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 00:30:12 2014

@author: matt
"""

# -*- coding: utf-8 -*-
"""
This script pulls in the location files from the LTRANSv2 output (llbounds.bln
and various para####.csv files). You can specify your starting particle 
locations by adjusting the 'Generate linear array' section. The test_loc.csv 
file is a two column  csv file containing your latitude longitude coordinates 
for the 'Generate linear array' section. To adjust the output file location
and name, see the 'Write output' section.

output:
    image: location plot
    test_loc.csv
    
    
Created on Mon Mar 10 18:15:44 2014

@author: mathew biddle
"""

import matplotlib.pyplot as plt # plotting
import numpy as np # numerical
import csv # output writing

# import data
coast = np.loadtxt('C:\Users\matt\Documents\umd\spring_2014\MEES616\testing\boundary.csv',delimiter=',')
start = np.loadtxt('C:\Users\matt\Documents\umd\spring_2014\MEES616\testing\para10000002.csv',delimiter=',')
#end = numpy.loadtxt('C:\Users\matt\Documents\umd\spring_2014\MEES616\class_20140306\para10000015.csv',delimiter=',')

# subplots
#plt.subplot(2,1,1)
#plt.plot(coast[:,0],coast[:,1],'b-',markersize=3)
#plt.plot(start[:,2],start[:,3],'r.',markersize=1)
#plt.grid(True)
#plt.subplot(2,1,2)
#plt.plot(coast[:,0],coast[:,1],'b-',markersize=3)
#plt.plot(end[:,2],end[:,3],'g.',markersize=1)
#plt.grid(True)
#plt.show()

## Generate linear array
#particles = 30000
#size = np.floor(np.sqrt(particles)) #calculate the grid size for lat lon
#lat = np.linspace(39.1,39.25,size) # generate even grid lat
#lon = np.linspace(-76.3,-76.35,size) # generate even grid lon
#lati,loni = np.meshgrid(lat,lon) # create the meshgrid

## Generate random array
#lat = np.random.uniform(39,39.56,170)
#lon = np.random.uniform(-76.46,-75.95,170)
#lati,loni = np.meshgrid(lat,lon)

# Plotting routines
plt.plot(coast[:,0],coast[:,1],'k-',markersize=1)
plt.plot(end[:,2],end[:,3],'g.',markersize=1)
#plt.plot(loni.flatten(),lati.flatten(),'g.')
#plt.scatter(loni,lati,s=.1,c='g',marker='o',lw=0)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Chesapeake Bay Initial Particle Locations')
plt.minorticks_on()
plt.grid(b=None,which='major',axis='both')
plt.show()

## Write output
#lontest = loni.flatten() # creates vector
#lattest = lati.flatten()
#output = lattest + lontest
#ofile = open('test_loc.csv','wb') # creates output file
#writer = csv.writer(ofile,delimiter=',') # describes what it will look like
#rows = zip(loni.flatten(), lati.flatten()) # write all rows at once
#writer.writerows(rows) # write rows
#ofile.close() # close file


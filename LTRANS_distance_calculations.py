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
import scipy.stats as stats
from matplotlib.ticker import MaxNLocator

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
stds = []
stderr = []
alldistances = []
spread_distance = []
whatplot = 'bargraphspread'#'bargraphavgdist' #'scattergraph' # 'none' # 'bargraphspread'
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
indx=0
## work through each diretory
for j in paths:
    indx = indx+1
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
                    
        elif i == 'para10000002.csv': # first model run
            #filenames = "C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\sand_test_1997_2014_04_07\%s" % i
            filenames = "%s\%s" % (j, i)
            #print "processing: %s" % filenames
            with open(filenames, 'rb') as f:
                reader = csv.reader(f)
                for row in reader:
                    depth_start.append(float(row[0]))
                    code_start.append(float(row[1]))
                    lon_start.append(float(row[2]))
                    lat_start.append(float(row[3]))
## Calculate distances between points, each row is the same particle
    for k in range(len(lon_start)):
        #distance.append(haversine_mine.distance([lon_start[k],lat_start[k]],[lon_end[k],lat_end[k]]))
        distance.append(haversine_mine.distance([lat_start[k],lon_start[k]],[lat_end[k],lon_end[k]]))
    #print "start:  %f %f" % (lon_start[k],lat_start[k])
        #print min(lat_end)
        #print max(lat_end)
    #print "end:    %f %f" % (lon_end[k],lat_end[k])
        #print "distance: %f" % distance[k]
    #print len(distance)
## Print statistics
#    print "Run: %s" % os.path.basename(j)
#    print "mean: %f km" % np.mean(distance)
    averages.append(np.mean(distance))
#    print "max: %f km" % max(distance)
    maximums.append(max(distance))
#    print "min: %f km" % min(distance)
    minimums.append(min(distance))
#    print "std: %f" % np.std(distance)
    stds.append(np.std(distance))
#    print "stderr: %f" % (np.std(distance)/np.sqrt(len(distance)))
    stderr.append(np.std(distance)/np.sqrt(len(distance)))
        
## Calculate spread
    #print 'min'
    min_lat_end = min(lat_end)
    south_point_lat = lat_end[lat_end.index(min_lat_end)]
    #south_point_lat.appped(lat_end[lat_end.index(min_lat_end)])
    south_point_lon = lon_end[lat_end.index(min_lat_end)]
    #south_point_lon.append(lon_end[lat_end.index(min_lat_end)])
    #print 'max'
    max_lat_end = max(lat_end)
    north_point_lat = lat_end[lat_end.index(max_lat_end)]
    north_point_lon = lon_end[lat_end.index(max_lat_end)]
    #spread_distance = haversine_mine.distance([north_point_lat,north_point_lon],[south_point_lat,south_point_lon])
    spread_distance.append(haversine_mine.distance([north_point_lat,north_point_lon],[south_point_lat,south_point_lon]))
    #print "%s\nSpread distance (km) = %f" % (filenames,spread_distance)
    print spread_distance
## reset variables
    depth_start = []
    code_start = []
    lon_start = []
    lat_start = []
    depth_end = []
    code_end = []
    lon_end = []
    lat_end = []
    alldistances.insert(indx,distance)
    distance = []
    print "\n"
#plt.plot(distance)
#plt.show()
print "sand 1997 %f" % np.mean(alldistances[0])
print "silt 1997 %f" % np.mean(alldistances[1])
print "clay 1997 %f" % np.mean(alldistances[2])
print "sand 1998 %f" % np.mean(alldistances[3])
print "silt 1998 %f" % np.mean(alldistances[4])
print "clay 1998 %f" % np.mean(alldistances[5])


if whatplot == 'scattergraph':
    #sediment_diam_meters = [1.016,0.0192,0.0032] # sand,silt,clay
    sand_diam_mm = [1.016] * len(alldistances[0])
    silt_diam_mm = [0.0192] * len(alldistances[1])
    clay_diam_mm = [0.0032] * len(alldistances[2])
    lowflowdist = alldistances[0] + alldistances[1] + alldistances[2]
    #lowflowdata[:] = [x*1000 for x in lowflowdata] # convert to m
    highflowdist = alldistances[3] + alldistances[4] + alldistances[5]
    #highflowdata[:] = [x*1000 for x in highflowdata] # convert to m
    grainsize = sand_diam_mm + silt_diam_mm + clay_diam_mm
    #grainsize[:] = [x*.000001 for x in grainsize] # convert to km

    f, ((ax1, ax2)) = plt.subplots(2,1,figsize=(10,7),sharex='col')#sharey='row')#,figsize=(10,20), sharex='col', sharey='row')
    # plot scatter plot (size,avgdistance)
    # low flow
    slopel, interceptl, r_valuel, p_valuel, std_errl = stats.linregress(grainsize,lowflowdist)
    linel = [slopel*x+interceptl for x in grainsize]
    ax1.plot(grainsize,lowflowdist,'b.',grainsize,linel,'r-')
    ax1.axis([min(grainsize)-.035, max(grainsize)+.035, min(highflowdist)-5, max(highflowdist)+5])
    ax1.text(.6,60,'y = %6.4fx + %6.4f\nR$^2$ = %6.4f'%(slopel,interceptl,r_valuel**2))
    ax1.text(1,140,'A')
    #ax1.set_xlabel('Grain Size [mm]')
    ax1.set_ylabel('Distance [km]')
    ax1.grid(b=None,which='major',axis='both')
    #ax1.set_title('Aug 1-10, 1997')
    #x = []
    # high flow
    slopeh, intercepth, r_valueh, p_valueh, std_errh = stats.linregress(grainsize,highflowdist)
    lineh = [slopeh*x+intercepth for x in grainsize]
    ax2.plot(grainsize,highflowdist,'b.',grainsize,lineh,'r-')
    ax2.axis([min(grainsize)-.035, max(grainsize)+.035, min(highflowdist)-5, max(highflowdist)+5])
    ax2.text(.6,50,'y = %6.4fx + %6.4f\nR$^2$ = %6.4f\n'%(slopeh,intercepth,r_valueh**2))
    ax2.text(1,140,'B')
    ax2.set_ylabel('Distance [km]')
    ax2.set_xlabel('Grain Size [mm]')
    ax2.grid(b=None,which='major',axis='both')
    
    wspace = 0.05 
    f.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=wspace)
    nbins = len(ax1.get_yticklabels()) # added 
    #ax2.yaxis.set_major_locator(MaxNLocator(nbins=nbins, prune='upper'))
    #ax2.set_title('May 10-20, 1998')
   # plt.savefig("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\\distance_size_scatter.png",dpi=200)
## plot average distance bar  chart
if whatplot == 'bargraphavgdist':
    lowflowavg = averages[0:3]
    lowflowmin = minimums[0:3]
    lowflowmax = maximums[0:3]
    lowflowstd = stds[0:3]
    lowflowstderr = stderr[0:3]
    highflowavg = averages[3:7]
    highflowmin = minimums[3:7]
    highflowmax = maximums[3:7]
    highflowstd = stds[3:7]
    highflowstderr = stderr[0:3]
    x = [1,2,3]
    x1 = [.85,1.85,2.85]
    x2 = [1.15,2.15,3.15]
    ax = plt.subplot(1,1,1)
    low = ax.bar(x1,lowflowavg,width=0.3,color='b',align='center',yerr=lowflowstderr,ecolor='k')
    high = ax.bar(x2,highflowavg,width=0.3,color='g',align='center',yerr=highflowstderr,ecolor='k')
    #ax.legend( (low[0], high[0]),('Aug 1-10 1997','May 10-20 1998'),loc = 2)
    ax.set_xticks(x)
    ax.set_xticklabels(['Sand','Silt','Clay'])
    ax.grid(b=None,which='major',axis='y')
    plt.ylabel('Average Distance Traveled [km]')
    plt.xlabel('Sediment Class')
    plt.tight_layout()
    plt.savefig("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\\average_distance_bar_nolegend.png",dpi=200)
## Plot bar of particle spread at final run.
if whatplot == 'bargraphspread':
    lowflowspread = spread_distance[0:3]
    highflowspread = spread_distance[3:7]

    x = [1,2,3]
    x1 = [.85,1.85,2.85]
    x2 = [1.15,2.15,3.15]
    ax = plt.subplot(1,1,1)
    low = ax.bar(x1,lowflowspread,width=0.3,color='b',align='center')#,yerr=lowflowstderr,ecolor='k')
    high = ax.bar(x2,highflowspread,width=0.3,color='g',align='center')#,yerr=highflowstderr,ecolor='k')
    #ax.legend( (low[0], high[0]),('Aug 1-10 1997','May 10-20 1998'),loc = 2)
    ax.set_xticks(x)
    ax.set_xticklabels(['Sand','Silt','Clay'])
    ax.grid(b=None,which='major',axis='y')
    plt.ylabel('Spread Distance [km]')
    plt.xlabel('Sediment Class')
    plt.tight_layout()
    plt.savefig("C:\Users\matt\Documents\umd\spring_2014\MEES616\project\my_project\data\\distance_spread_bar_nolegend.png",dpi=200)
plt.show()

'''
Joshua Nolan
924211436@gsc.edu
'''

from osgeo import gdal
from numpy import *
import glob,os,shutil
import fnmatch

##Create ndsm rasters from a dem and dsm rasters

##Inputs
dem_folder = raw_input("Please input the file path to the DEM folder here: ")
dsm_folder = raw_input("Please input the file path to the DSM folder here: ")
output = raw_input("Please input the file path to the output folder here: ")
                   
##Go through the DEM folder and store all dems in a list
dem_list = []
for root,dir,filename in os.walk(dem_folder):
    for filename in fnmatch.filter(filename,"*.tif"):
        dem_list.append(filename)

##Go through output folder and create list of ndsms
ndsm_list = []
for root,dir,filename in os.walk(output):
    for filename in fnmatch.filter(filename,"*.tif"):
        filenames = filename.split('n')
        ndsm_list.append(filenames[0])

##Figure out what ndsms have been made to make new list of one that have not
##been made
diff_list = []
for item in dem_list:
    items = item.split('d')
    items = items[0]
    if not items in ndsm_list:
        diff_list.append(item)
        
##For each item in the list it will open the item and then find the same name of
##of that file in another folder and subtract to the two files to create the product
ndsm_list = []
for item in diff_list:
    item_fixed = dem_folder + '\\' + item
    image = gdal.Open(item_fixed)
    cols = image.RasterXSize
    rows = image.RasterYSize
    proj = image.GetProjection()
    datum = image.GetGeoTransform()
    for root,dir,filename in os.walk(dsm_folder):
        for filename in fnmatch.filter(filename,"*.tif"):
            if filename.split('d')[0] == item.split('d')[0]:
                name = dsm_folder + '\\' + filename
                image2 = gdal.Open(name)
                dsm = image2.GetRasterBand(1).ReadAsArray()
                dem = image.GetRasterBand(1).ReadAsArray()
                dsm = array(dsm, dtype = float)
                dem = array(dem, dtype = float)
                ndsm = subtract(dsm,dem)
                driver = gdal.GetDriverByName('GTiff')
                items = item.split('d')
                items = items[0] + 'ndsm.tif'
                nDSM = driver.Create(items, cols, rows, 1, gdal.GDT_Float32)
                nDSM.SetGeoTransform(datum)
                nDSM.SetProjection(proj)
                nDSM.GetRasterBand(1).WriteArray(ndsm)
                stat = nDSM.GetRasterBand(1).GetStatistics(1,1)
                nDSM.GetRasterBand(1).SetStatistics(stat[0], stat[1], stat[2], stat[3])
                ndsm_list.append(items)
                print items
            else:
                pass
            
##Let the user know you are now moving the files
print"Moving files"

##We need to isolate only the ndsm files since those are the files that we want to move.
del nDSM
for item in ndsm_list:
    shutil.move(item,output)

##When everything is done print "DONE" so the user knows the program has finished.
print "DONE"


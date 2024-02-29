import sys, os, arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True

wd = raw_input('In which directory are your image files located?')
satellite = raw_input('With which Landsat Satellite was your imagery acquired? (5,7,8)')
date = raw_input('Was your image collected before of after May 31, 2003? (before/after)').lower()

arcpy.env.workspace = wd
raster_list=arcpy.ListRasters("", "tif")



if satellite == '7' and date == 'after':
    os.chdir(wd)
    os.makedirs('SC_Corr')
    for Ras in raster_list:
        arcpy.AddMessage("Processing" + Ras)
        desc = arcpy.Describe(Ras)
        if desc.bandCount == 1:
            arcpy.SetRasterProperties_management(Ras, nodata="1 0")
            Con(IsNull(Ras), FocalStatistics(Ras, NbrRectangle(15,15,"CELL"),"MEAN"),Ras).save(wd + '\SC_Corr\CORR_{}'.format(Ras))
    cd = wd + "\SC_Corr"
    arcpy.env.workspace = cd
    corr_list=arcpy.ListRasters("","tif")
    comp_images = [raster for raster in corr_list[0:5]]
    comp_images.append(corr_list[7])

    
elif satellite == '7' and date == 'before':
    comp_images = [raster for raster in raster_list[0:5]]
    comp_images.append(raster_list[7])    
    
    
elif satellite == '8':
    comp_images= [raster_list[0]]
    comp_images += raster_list[3:10]
    
    
elif satellite == '5':
    comp_images = [raster for raster in raster_list[0:5]]
    comp_images.append(raster_list[6])


arcpy.CompositeBands_management(comp_images, "Final_Composite.tif")


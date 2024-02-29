import arcpy
from arcpy import env
from arcpy.sa import *

#Clip Raster to smaller area for faster processing

    # Set outputs to be overwritten just in case; each subprocess gets its own environment settings
arcpy.env.overwriteOutput=True
    # Set workspace
arcpy.env.workspace = r"C://sys"

    #Clip Raster Dataset with feature geometry
arcpy.Clip_management("highres.sid", "#", "highrescl.img", "Area_Poly.shp", "0", "ClippingGeometry")
    
    # Clean up the in-memory workspace
arcpy.Delete_management("in_memory")

#Extract area of interst by mask from smaller area


    # Set local variable
inRaster = "highrescl.img"
inMaskData = "jekyllshppoly11.shp"

    # Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

    # Extract by mask
outExtractByMask = ExtractByMask(inRaster, inMaskData)
outExtractByMask.save("jekylmask")    
    # Clean up the in-memory workspace
arcpy.Delete_management("in_memory")

##Convert Raster to TIFF
arcpy.RasterToOtherFormat_conversion("jekylmask","c://sys","TIFF")

#Run Isocluster tool to develop clusters from raster and to output a sig file

    # Set local variables
inRaster = "jekylmask"
outSig = "hghresiso.gsg"
classes = 34
cycles = 20
minMembers = 20
sampInterval = 10
               
# Execute IsoCluster
IsoCluster(inRaster, outSig, classes, cycles, minMembers, sampInterval)
##outUnsupervised.save("hghresunsup1.tif")
  
    # Clean up the in-memory workspace
arcpy.Delete_management("in_memory")

##Maximum Likelihood Classification

    # Set local variables
inRaster = "jekylmask"
sigFile = "hghresiso.gsg"
probThreshold = "0.005"
aPrioriWeight = "EQUAL"
aPrioriFile = ""
outConfidence = "hghconf"                                  
               

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute 
mlcOut = MLClassify(inRaster, sigFile, probThreshold, aPrioriWeight, 
                    aPrioriFile, outConfidence) 

# Save the output 
mlcOut.save("hghresmlc")

##Convert MLC to TIFF

arcpy.RasterToOtherFormat_conversion("hghresmlc","c://sys","TIFF")

    # Clean up the in-memory workspace
arcpy.Delete_management("in_memory")

  ##Build Pyramids

    ##Define parameters for build pyramids and calculate statitics in environment setting
arcpy.env.pyramid = "PYRAMIDS 3 BILINEAR JPEG"
arcpy.env.rasterStatistics = "STATISTICS 4 6 (0)"
    
    ##Build pyramids and calculate statistics for all raster in a folder
arcpy.BuildPyramids_management("hghresmlc.tiff")
arcpy.BuildPyramids_management("jekylmask.tiff")
    
   

    # Clean up the in-memory workspace
arcpy.Delete_management("in_memory")

import arcpy
from arcpy import env
from arcpy.sa import *
import os
import math
import multiprocessing
import time

############################    Configuration:    ##############################
# Specify scratch workspace
scratchws = r"c:\temp\bldgshadowtest" # MUST be a folder, not a geodatabase!

# Specify output field name for the original FID
origfidfield = "ORIG_FID"

# Specify the number of processors (CPU cores) to use (0 to use all available)
cores = 0

# Specify per-process feature count limit, tune for optimal
# performance/memory utilization (0 for input row count divided by cores)
procfeaturelimit = 0

# TIP: Set 'cores' to 1 and 'procfeaturelimit' to 0 to avoid partitioning and
# multiprocessing completely
################################################################################

def message(msg, severity=0):
    print msg

    try:
        for string in msg.split('\n'):
            if severity == 0:
                arcpy.AddMessage(string)
            elif severity == 1:
                arcpy.AddWarning(string)
            elif severity == 2:
                arcpy.AddError(string)
    except:
        pass

def getOidRanges(inputFC, oidfield, count):
    oidranges = []
    if procfeaturelimit > 0:
        message("Partitioning row ID ranges ...")
        rows = arcpy.SearchCursor(inputFC, "", "", oidfield, "%s A" % oidfield)
        minoid = -1
        maxoid = -1
        for r, row in enumerate(rows):
            interval = r % procfeaturelimit
            if minoid < 0 and (interval == 0 or r == count - 1):
                minoid = row.getValue(oidfield)
            if maxoid < 0 and (interval == procfeaturelimit - 1 or r == count - 1):
                maxoid = row.getValue(oidfield)
            if minoid >= 0 and maxoid >= 0:
                oidranges.append([minoid, maxoid])
                minoid = -1
                maxoid = -1
        del row, rows
    return oidranges


    # Set outputs to be overwritten just in case; each subprocess gets its own environment settings
env.overwriteOutput=True
    # Set workspace
env.workspace = r"C://system"

    #Set local variable
inRaster = "highrescl2.img"
inMaskData = "jekyllshppoly11.shp"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")


outExtractByMask = ExtractByMask(inRaster, inMaskData)
outExtractByMask.save("jekylmask")    
    # Clean up the in-memory workspace
arcpy.Delete_management("in_memory")

    

##if __name__ == "__main__":
##    arcpy.env.overwriteOutput=True
##
##    # Read in parameters
##    inputFC = arcpy.GetParameterAsText(0)
##    outputFC = arcpy.GetParameterAsText(1)
##    heightfield = arcpy.GetParameterAsText(2) #Must be in the same units as the coordinate system!
##    azimuth = math.radians(float(arcpy.GetParameterAsText(3))) #Must be in degrees
##    altitude = math.radians(float(arcpy.GetParameterAsText(4))) #Must be in degrees
##
##    # Get field names
##    desc = arcpy.Describe(inputFC)
##    shapefield = desc.shapeFieldName
##    oidfield = desc.oidFieldName
##
##    count = int(arcpy.GetCount_management(inputFC).getOutput(0))
##    message("Total features to process: %d" % count)
##
##    #Export output spatial reference to string so it can be pickled by multiprocessing
##    if arcpy.env.outputCoordinateSystem:
##	outputSR = arcpy.env.outputCoordinateSystem.exportToString()
##    elif desc.spatialReference:
##	outputSR = desc.spatialReference.exportToString()
##    else:
##	outputSR = ""
##
##    # Configure partitioning
##    if cores == 0:
##	cores = multiprocessing.cpu_count()
##    if cores > 1 and procfeaturelimit == 0:
##	procfeaturelimit = int(math.ceil(float(count)/float(cores)))
##
##     # Start timing
##    start = time.clock()
##
##    # Partition row ID ranges by the per-process feature limit
##    oidranges = getOidRanges(inputFC, oidfield, count)
##
##    if len(oidranges) > 0: # Use multiprocessing
##	message("Computing shadow polygons; using multiprocessing (%d processes, %d jobs of %d maximum features each) ..." % (cores, len(oidranges), procfeaturelimit))
##
##	# Create a Pool of subprocesses
##	pool = multiprocessing.Pool(cores)
##	jobs = []
##
##	# Get the appropriately delmited field name for the OID field
##	oidfielddelimited = arcpy.AddFieldDelimiters(inputFC, oidfield)
##
##	# Ensure the scratch workspace folder exists
##	if not os.path.exists(scratchws):
##	    os.mkdir(scratchws)
##
##	for o, oidrange in enumerate(oidranges):
##	    # Build path to temporary output feature class (dissolved shadow polygons)
##	    # Named e.g. <scratchws>\dissolvedshadows0000.shp
##	    tmpoutput = os.path.join(scratchws, "%s%04d.shp" % ("dissolvedshadows", o))
##
##	    # Build a where clause for the given OID range
##	    whereclause = "%s >= %d AND %s <= %d" % (oidfielddelimited, oidrange[0], oidfielddelimited, oidrange[1])
##
##	    # Add the job to the multiprocessing pool asynchronously
##	    jobs.append(pool.apply_async(computeShadows, (inputFC, tmpoutput, oidfield, shapefield, heightfield, azimuth, altitude, outputSR, whereclause)))
##
##	# Clean up worker pool; waits for all jobs to finish
##	pool.close()
##	pool.join()
##
##	 # Get the resulting outputs (paths to successfully computed dissolved shadow polygons)
##	results = [job.get() for job in jobs]
##
##	try:
##	    # Merge the temporary outputs
##	    message("Merging temporary outputs into output feature class %s ..." % outputFC)
##	    arcpy.Merge_management(results, outputFC)
##	finally:
##	    # Clean up temporary data
##	    message("Deleting temporary data ...")
##	    for result in results:
##		message("Deleting %s" % result)
##		try:
##		    arcpy.Delete_management(result)
##		except:
##		    pass
##    else: # Use a single process
##	message("Computing shadow polygons; using single processing ...")
##	computeShadows(inputFC, outputFC, oidfield, shapefield, heightfield, azimuth, altitude, outputSR)
##
##    # Stop timing and report duration
##    end = time.clock()
##    duration = end - start
##    hours, remainder = divmod(duration, 3600)
##    minutes, seconds = divmod(remainder, 60)
##    message("Completed in %d:%d:%f" % (hours, minutes, seconds))

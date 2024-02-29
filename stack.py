from osgeo import gdal
import glob
## Open the Image and pull out some useful information

##counter = 1
##for filename in os.listdir('C:\\system\\ls2'):
##    basename, extension = filename.split('.')
##    fileid, band = basename.split('_B')
##    if extension = 'TIF'
##        band

tifs = glob.glob('*.tif')

counter = 1
for tif in tifs:
    image = gdal.Open(tif)
    if "_B1." in tif:
        cols = image.RasterXSize
        rows = image.RasterYSize
        proj = image.GetProjection()
        datum = image.GetGeoTransform()

        ## Create the output stacked image
        driver = gdal.GetDriverByName('GTiff')
        stacked_image = driver.Create("{0}.tif".format(tif.split('_')[0]),
                                      cols, rows, 7, gdal.GDT_Byte)
                                                                
        ## Set the datum and the projection
        stacked_image.SetGeoTransform(datum)
        stacked_image.SetProjection(proj)

    band = image.GetRasterBand(1).ReadAsArray()

    ## Write the data into the new image
    print tif.split('_')[0]
    stacked_image.GetRasterBand(counter).WriteArray(band)
    stat = stacked_image.GetRasterBand(counter).GetStatistics(1,1)
    stacked_image.GetRasterBand(counter).SetStatistics(stat[0], stat[1], stat[2], stat[3])
    counter += 1
    

 

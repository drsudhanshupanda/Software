forus = "17:39:27 PM"

##def correcttime(gpstime):
##  """Subtracting 1 hours to correct GPS time"""
##  if len(gpstime) is not 11:
##    listtime = list(gpstime)
##    listtime.append(' PM')
##    finaltime = "".join(listtime)
##  return finaltime
 
  
#str((listtime.append(" PM")))


def correcttime(gpstime):
  """Subtracting 4 hours to correct GPS time
  """
  if gpstime[0] == '1':
    ltime = list(gpstime)
    ltime[0] = '0'
    timeiswine = ''.join(ltime)
  return timeiswine

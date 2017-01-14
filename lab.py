import glob
import time
import os
def currentTime():
    return int(round(time.time()*1000))

startTime = currentTime()
print startTime
time.sleep(1)
endTime = currentTime()

print endTime
# print "project time: ",totalTime

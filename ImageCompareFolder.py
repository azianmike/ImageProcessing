__author__ = 'michaelluo'

from ImageCompare import compareImages2
import os
import time
from SendGCM import sendGCM

def compareAllImagesInFolder(folderName):
    print 'folderName'
    imageList = os.listdir(folderName)
    modifiedImageList = []
    for image in imageList:
        temp = [0,0, image]
        modifiedImageList.append(temp)

    returnList = []
    while(len(modifiedImageList)!=0):
        returnMe, modifiedImageList = compareImages2(modifiedImageList.pop()[2], modifiedImageList, folderName+'/')
        returnList.append(returnMe)
        # print 'returned that are similar ' + str(returnMe)
        # print 'returned that are not' + str(modifiedImageList)

    return returnList

def sendComparedImagesGCM(folderName, gcm_ID):
    returnedData = compareAllImagesInFolder(str(folderName))
    returnedDataModified = str(returnedData).replace('%','/')
    sendGCM(str(returnedDataModified), gcm_ID)

# start_time = time.time()
# sendComparedImagesGCM(str(102436))
#
#
# print str(time.time() - start_time)
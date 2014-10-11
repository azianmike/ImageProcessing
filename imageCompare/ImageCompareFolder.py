__author__ = 'michaelluo'

import os
import time

from imageCompare.ImageCompare import compareImages2
from SendGCM import sendGCM


def compareAllImagesInFolder(folderName):
    imageList = os.listdir(folderName)
    imageList.sort(key=lambda x: os.path.getmtime(folderName+x))
    imageList.reverse()
    modifiedImageList = []
    for image in imageList:
        temp = [0,0, image]
        modifiedImageList.append(temp)

    returnList = []
    while(len(modifiedImageList)!=0):
        returnMe, modifiedImageList = compareImages2(modifiedImageList.pop()[2], modifiedImageList, folderName+'/')
        returnList.append(returnMe)

    return returnList

def sendComparedImagesGCM(folderName, gcm_ID):
    start_time = time.time()
    returnedData = compareAllImagesInFolder(str(folderName))
    returnedDataModified = str(returnedData).replace('%','/')
    sendGCM(str(returnedDataModified), gcm_ID)
    print str(time.time() - start_time)

# start_time = time.time()
# sendComparedImagesGCM(str(102436))
#
#
# print str(time.time() - start_time)
__author__ = 'michaelluo'

from ImageCompare import compareImages2
import os
import time

def compareAllImagesInFolder(folderName):
    print 'folderName'
    imageList = os.listdir(folderName)
    modifiedImageList = []
    for image in imageList:
        temp = [0,0, image]
        modifiedImageList.append(temp)

    while(len(modifiedImageList)!=0):
        returnMe, modifiedImageList = compareImages2(modifiedImageList.pop()[2], modifiedImageList, folderName+'/')

        print 'returned that are similar ' + str(returnMe)
        print 'returned that are not' + str(modifiedImageList)

start_time = time.time()
compareAllImagesInFolder(str(102436))

print str(time.time() - start_time)
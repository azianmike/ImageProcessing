__author__ = 'michaelluo'

import os
import base64
from PublicIP import getPublicIP
from shutil import rmtree

def saveImageData(data):

    try:
        userIDFolder = '/var/www/sampleapp/ImageProcessing/' + str(data['userID'])
        firstTime = data['firstTime']
        if firstTime == True: #clean up folder
            exceptionFolder = userIDFolder
            print 'cleaning up folder ' + str(exceptionFolder)
            deleteFiles(exceptionFolder)
        imageArray = data['image']
        firstImage = imageArray[0]
        imagesLeft = data['images left']  #if 0, call imagecompare on folder


        returnFolder = -1
        if imagesLeft == 0:
            returnFolder = userIDFolder


        filename = firstImage.keys()[0]
        if not os.path.isdir(userIDFolder):
            os.mkdir(userIDFolder)
        print filename
        imgData = base64.b64decode(firstImage[filename])
        imgIndx = filename.rfind('/')
        imgName = filename.replace('/', '%')

        dirName = userIDFolder+'/'+imgName
        with open(dirName, 'wb') as f:
            f.write(imgData)

        public_ip = getPublicIP()
        return str(public_ip), str(returnFolder)
    except Exception as inst:
        return inst, inst


def deleteFiles(returnFolder):
    try:
        print 'delete all files in ' + str(returnFolder)
        if os.path.isdir(returnFolder):  #deletes files in folder to save space
            rmtree(returnFolder)
    except Exception, e:
        print e

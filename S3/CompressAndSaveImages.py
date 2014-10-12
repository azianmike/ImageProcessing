__author__ = 'michaelluo'

import os
from PIL import Image
from S3 import uploadImageToS3Bucket, uploadListOfImagesToS3

def compressImages(folderName):
    newFileNames = []
    if not folderName.endswith('/'):
        folderName = folderName + '/'

    for file in os.listdir(folderName):
        if file.endswith('.jpg') or file.endswith('.png'):
            testImage = Image.open(folderName+file)
            (width, height) = testImage.size
            if (width > 3000 or height > 3000) :  #resize
                newWidth = int(width*.5)
                newHeight = int(height*.5)
                testImage.thumbnail((newWidth,newHeight),Image.ANTIALIAS)

            else:
                if(width > 1000 or height > 1000):
                    newWidth = int(width*.7)
                    newHeight = int(height*.7)
                    testImage.thumbnail((newWidth,newHeight),Image.ANTIALIAS)
                else:
                    testImage.thumbnail((width,height),Image.ANTIALIAS)

            newTestImageName = folderName+'Compressed_'+file
            testImage.save(newTestImageName, quality=50)
            newFileNames.append(newTestImageName)

    return newFileNames

def saveImagesToS3(compressedImagePaths):
    return uploadListOfImagesToS3(compressedImagePaths)

def compressAndSaveImages(userName):
    compressedImagePaths = compressImages(userName)
    print 'CompressedImagePaths-'
    print compressedImagePaths
    urlAndKeys = saveImagesToS3(compressedImagePaths)
    return urlAndKeys



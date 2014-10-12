__author__ = 'michaelluo'

from PIL import Image
import os, time
# testImage = Image.open('testImages/IMG_20141005_123558696_HDR.jpg')
# (width, height) = testImage.size
# print (width,height)
# newWidth = int(width*.6)
# newHeight = int(height*.6)
# size = (newWidth,newHeight)
# testImage.thumbnail(size,Image.ANTIALIAS)
# testImage.save('testImages/New_IMG_20141005_123558696_HDR.jpg', quality=40)
start_time = time.time()

def compressImages(folderName):
    newFileNames = []
    for file in os.listdir(folderName):
        if file.endswith('.jpg'):
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
                    testImage.thumbnail((newWidth,newHeight),Image.ANTIALIAS)

            newTestImageName = folderName+'New_'+file
            testImage.save(newTestImageName, quality=50)
            newFileNames.append(newTestImageName)

    return newFileNames

newNames = compressImages('testImages/')

print("--- %s seconds ---" % str(time.time() - start_time))
print newNames
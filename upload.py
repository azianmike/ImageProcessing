__author__ = 'michaelluo'

from saveImageData import saveImageData, deleteFiles
from ImageCompareFolder import sendComparedImagesGCM

def upload(data):
    successful, returnFolder = saveImageData(data)
    gcm_ID = data['gcm_ID']
    if returnFolder != '-1':
        print 'DONE!' + str(returnFolder)
        sendComparedImagesGCM(str(returnFolder), gcm_ID)
        #storeUserNumberOfImages(data, returnFolder)
        deleteFiles(returnFolder)
    return (successful + '\n')
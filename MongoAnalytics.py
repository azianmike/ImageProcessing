__author__ = 'michaelluo'

from pymongo import MongoClient



def storeUserNumberOfImages(data, folderName):
    client = MongoClient('localhost', 27017)  #connecting to mongodb on localhost
    numOfFiles = getNumberOfFiles(folderName)
    db = client['images'].number  #connecting to the userDB database, then going to 'users' collection
    userID = data['userID']
    gcm_ID = data['gcm_ID']

    numOfImages = {'gcm':gcm_ID, 'userID':userID, 'numOfImages':numOfFiles}
    db.insert(numOfImages)

def getNumberOfFiles(folderName):
    import os
    from shutil import rmtree

    try:
        print 'delete all files in ' + str(folderName)
        if os.path.isdir(folderName):  #deletes files in folder to save space
            #toDO
            #return number of files in folderName
            print 'nothing'
    except Exception, e:
        print e
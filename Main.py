__author__ = 'michaelluo'

import socket
import base64
import os
import json
import shutil
from pymongo import MongoClient
from ImageCompareFolder import sendComparedImagesGCM
from multiprocessing import Process
from PublicIP import getPublicIP

def readJSON():
    try:
        print 'reading in json data'
        data = ''
        while (1):
            dataRecv = conn.recv(2048)
            if(len(dataRecv) == 0):
                raise Exception("caught timeout")
            data += dataRecv
            if '\r\n\r\n' in dataRecv:
                print 'stopped reading in json'
                break;

        return data[:-4]
    except:
        print 'caught timeout while reading'

def saveImageData(data):

    userIDFolder = data['userID']
    imageArray = data['image']
    firstImage = imageArray[0]
    imagesLeft = data['images left']  #if 0, call imagecompare on folder


    returnFolder = -1
    print imagesLeft
    if imagesLeft == 0:
        returnFolder = userIDFolder


    filename = firstImage.keys()[0]
    if not os.path.isdir(userIDFolder):
        os.mkdir(userIDFolder)
    print filename
    imgData = base64.b64decode(firstImage[filename])
    #imgdata = data
    imgIndx = filename.rfind('/')
    imgName = filename.replace('/', '%')

    dirName = userIDFolder+'/'+imgName
    with open(dirName, 'wb') as f:
        f.write(imgData)

    public_ip = getPublicIP()
    return str(public_ip), str(returnFolder)


def register(data):
    print 'register'
    client = MongoClient('localhost', 27017)  #connecting to mongodb on localhost

    db = client['userDB'].users  #connecting to the userDB database, then going to 'users' collection
    userEmail = data['user_email']
    password = data['password']
    gcm_ID = data['gcm_ID']
    firstOne = db.find_one({'email':userEmail})  #finding the first one
    if firstOne is None: #means email does not exist in db, add into db
        lastUserID = db.find().sort('userID', -1).limit(1)
        lastUserNUM = int(lastUserID[0]['userID'])+1
        testEmail = {'email':userEmail, 'userID':lastUserNUM, 'password':password, 'gcm_ID':gcm_ID}
        db.insert(testEmail)
        return '1'
    else:
        return '0'

def login(data):
    print 'register'
    print data
    client = MongoClient('localhost', 27017)  #connecting to mongodb on localhost
    print '1'
    db = client['userDB'].users  #connecting to the userDB database, then going to 'users' collection
    print '2'
    userEmail = data['user_email']
    password = data['password']
    firstOne = db.find_one({'email':userEmail, 'password':password})  #finding the first one
    print '3'
    if firstOne is None: #means email does not exist in db, add into db
        print 'returns'
        return '-1'
    else:
        print 'returns'
        return str(firstOne['userID'])

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 5069))
#become a server socket
serversocket.listen(5)


def connAccepted(conn):
    try:
        data = json.loads(readJSON())
        if data['function'] == 'register':
            successful = register(data)
            conn.send(successful+'\n')
        elif data['function'] == 'login':
            successful = login(data)
            print successful
            conn.send(successful+'\n')
            print 'done sending'
        elif data['function'] == 'upload':
            successful, returnFolder = saveImageData(data)
            conn.send(successful+'\n')
            gcm_ID = data['gcm_ID']
            if returnFolder != '-1':
                print 'DONE!' + str(returnFolder)
                sendComparedImagesGCM(returnFolder, gcm_ID)
                try:
                    print 'delete all files'
                    if os.path.isdir(returnFolder):  #deletes files in folder to save space
                        shutil.rmtree(returnFolder)
                except Exception, e:
                    print e
        conn.close()
    except:
        print 'caught timeout'
        exit(1)

while 1:
    #accept connections from outside
    print 'listening for data'
    (conn, address) = serversocket.accept()

    print 'accepted'
    print conn
    p = Process(target=connAccepted, args=(conn,))
    p.start()
    print 'process id:' + str(p.pid)


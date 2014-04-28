__author__ = 'michaelluo'

import socket
import base64
import os
import json
from pymongo import MongoClient

def readJSON():
    data = ''
    while (1):
        dataRecv = conn.recv(1024)
        data += dataRecv
        if '\r\n\r\n' in dataRecv:
            print 'broken'
            break;

    return data[:-4]


def saveImageData(data):

    userIDFolder = data['userID']
    imageArray = data['image']
    firstImage = imageArray[0]

    filename = firstImage.keys()[0]
    if not os.path.isdir(userIDFolder):
        os.mkdir(userIDFolder)
    print filename
    imgData = base64.b64decode(firstImage[filename])
    #imgdata = data
    imgIndx = filename.rfind('/')
    imgName = filename[imgIndx + 1:]

    dirName = userIDFolder+'/'+imgName
    with open(dirName, 'wb') as f:
        f.write(imgData)
    print 'done writing image'
    return '1'


def register(data):
    print 'register'
    print data
    client = MongoClient('localhost', 27017)  #connecting to mongodb on localhost

    db = client['userDB'].users  #connecting to the userDB database, then going to 'users' collection
    userEmail = data['user_email']
    password = data['password']
    firstOne = db.find_one({'email':userEmail})  #finding the first one
    if firstOne is None: #means email does not exist in db, add into db
        lastUserID = db.find().sort('userID', -1).limit(1)
        lastUserNUM = int(lastUserID[0]['userID'])+1
        testEmail = {'email':userEmail, 'userID':lastUserNUM, 'password':password}
        db.insert(testEmail)
        return '1'
    else:
        return '0'

def login(data):
    print 'register'
    print data
    client = MongoClient('localhost', 27017)  #connecting to mongodb on localhost

    db = client['userDB'].users  #connecting to the userDB database, then going to 'users' collection
    userEmail = data['user_email']
    password = data['password']
    firstOne = db.find_one({'email':userEmail, 'password':password})  #finding the first one
    if firstOne is None: #means email does not exist in db, add into db
        return '-1'
    else:
        return str(firstOne['userID'])

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 5069))
#become a server socket
serversocket.listen(5)

while 1:
    #accept connections from outside
    print 'listening for data'
    (conn, address) = serversocket.accept()
    print 'accepted'
    print conn



    data = json.loads(readJSON())
    if data['function'] == 'register':
        successful = register(data)
        conn.send(successful)
    elif data['function'] == 'login':
        successful = login(data)
        conn.send(successful)
    elif data['function'] == 'upload':
        successful = saveImageData(data)
        conn.send(successful)
    #saveImageData(data)


    conn.close()
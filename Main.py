__author__ = 'michaelluo'

from ImageCompare import compareImagesToDB
import time
import socket
import base64
import os.path
import json
from pymongo import MongoClient
test_pic = 'SimilarNoFlash.jpg' #testing this pic against all pics in our db;
db = [

    [0, 0, 'KindaSimilar1.jpg'],
    [0, 0, 'KindaSimilar2.jpg'],
    [0, 0, 'island.jpg'],
    [0, 0, 'Rose1.jpg'],
    [0, 0, 'Rose2.jpg'],
    [0, 0, 'Different.jpg'],
    [0, 0, 'DifferentSubject.jpg'],
    [0, 0, 'Similar2.jpg'],
    [0, 0, 'SimilarNoFlash.jpg'],
    [0, 0, 'Similar1.jpg']
    ]

def getSimilarImages():
    start_time = time.time()

# returnMe, db2 = compareImagesToDB(db.pop()[2], db)
# print 'returned that are similar ' + str(returnMe)
# print 'returned that are not' + str(db2)
# compareImagesToDB(db2.pop()[2], db2)
# print '--------------------'
# compareImagesToDB(test_pic, db2)
# print '---------------------'
# compareImagesToDB(test_pic, db2)
# print '---------------------'
# compareImagesToDB(test_pic, dbtest)
    while(len(db)!=0):
        returnMe, db = compareImagesToDB(db.pop()[2], db)
        print 'returned that are similar ' + str(returnMe)
        print 'returned that are not' + str(db)

    print str(time.time() - start_time) + " seconds"

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 5069))
#become a server socket
serversocket.listen(5)
print 'listening'


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

    print data[0]
    print data[1].keys()
    #data = conn.recv(102)
    print 'done listening for data'
    #print data
    filename = data[1].keys()[0]
    imgdata = base64.b64decode(data[1][filename])
    #imgdata = data
    imgIndx = filename.rfind('/')
    imgName = filename[imgIndx + 1:]
    with open(imgName, 'wb') as f:
        f.write(imgdata)

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
    #saveImageData(data)


    conn.close()
__author__ = 'michaelluo'

from pymongo import MongoClient

def register(data):
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
    db = client['userDB'].users  #connecting to the userDB database, then going to 'users' collection
    userEmail = data['user_email']
    password = data['password']
    firstOne = db.find_one({'email':userEmail, 'password':password})  #finding the first one
    if firstOne is None: #means email does not exist in db, add into db
        print 'returns'
        return '-1'
    else:
        print 'returns'
        return str(firstOne['userID'])
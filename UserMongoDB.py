__author__ = 'michaelluo'

from pymongo import MongoClient


client = MongoClient('localhost', 27017)  #connecting to mongodb on localhost

db = client['userDB'].users  #connecting to the userDB database, then going to 'users' collection
print db

email = 'tes3t@email.com'

firstOne = db.find_one({'email':email})  #finding the first one
print firstOne

lastUserID = db.find().sort('userID', -1).limit(1)
print lastUserID[0]['userID']

lastUserNUM = int(lastUserID[0]['userID'])+1



testEmail = {'email':email, 'userID':lastUserNUM}
db.insert(testEmail)

foundAll = db.find()
for post in foundAll:
    print post
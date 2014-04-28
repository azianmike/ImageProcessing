__author__ = 'michaelluo'

import time
from ImageCompare import compareImagesToDB
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


start_time = time.time()
lengthOfArray = len(db)
client = MongoClient('localhost', 27017)  #connecting to mongodb on localhost

db = client['userDB'].imageData

while(len(db)!=0):
    returnMe, db = compareImagesToDB(db.pop()[2], db)

    # print 'returned that are similar ' + str(returnMe)
    # print 'returned that are not' + str(db)

print str(time.time() - start_time) + " seconds for " + str(lengthOfArray)
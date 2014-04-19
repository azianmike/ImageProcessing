__author__ = 'michaelluo'

from ImageCompare import compareImagesToDB
import time
from PIL import Image

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
#print db[0][2]

returnMe, db2 = compareImagesToDB(db.pop()[2], db)
print 'returned that are similar ' + str(returnMe)
print 'returned that are not' + str(db2)
compareImagesToDB(db2.pop()[2], db2)
print '--------------------'
compareImagesToDB(test_pic, db2)
print '---------------------'
compareImagesToDB(test_pic, db2)
print '---------------------'
compareImagesToDB(test_pic, db)


print str(time.time() - start_time) + " seconds"
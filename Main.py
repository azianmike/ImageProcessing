__author__ = 'michaelluo'

from ImageCompare import compareImagesToDB
import time
from PIL import Image

test_pic = 'Similar1.jpg' #testing this pic against all pics in our db;
db = [
    [0, 0, 'Similar1.jpg'],
    [0, 0, 'KindaSimilar1.jpg'],
    [0, 0, 'KindaSimilar2.jpg'],
    [0, 0, 'island.jpg'],
    [0, 0, 'Rose1.jpg'],
    [0, 0, 'Rose2.jpg'],
    [0, 0, 'Different.jpg'],
    [0, 0, 'DifferentSubject.jpg'],
    [0, 0, 'Similar1.jpg'],
    [0, 0, 'Similar2.jpg'],
    [0, 0, 'SimilarNoFlash.jpg'],
    ]

start_time = time.time()
#print db[0][2]
compareImagesToDB(test_pic, db)

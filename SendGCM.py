from gcm import GCM
import sys
from pymongo import MongoClient


def sendGCM(data, gcm_ID):
    client = MongoClient('localhost', 27017)  #connecting to mongodb on localhost

    db = client['userDB'].users  #connecting to the userDB database, then going to 'users' collection


    API_KEY = 'AIzaSyD7pWKO8wqOGwD6nNIYqR43mJU3Ro56qGY'

    gcm = GCM(API_KEY)

    if sys.getsizeof(data) > 3800:
        data = 'refresh'
    data2 = {'data': data}

    # Plaintext request

    gcm.plaintext_request(registration_id=gcm_ID, data=data2)
    print 'sent GCM for ' + str(gcm_ID)

# listTest = ['hi', 'hi2']
#
# sendGCM(str(listTest))
#
# returnedData = ''
# for i in range(4000):
#     returnedData += 'a'
# print sys.getsizeof(returnedData)
# sendGCM(returnedData)

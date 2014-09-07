from gcm import GCM
import sys

def sendGCM(data, gcm_ID):
    API_KEY = 'AIzaSyD7pWKO8wqOGwD6nNIYqR43mJU3Ro56qGY'

    gcm = GCM(API_KEY)

    if sys.getsizeof(data) > 3800:
        data = 'refresh'
    data2 = {'data': data}

    # Plaintext request

    response = gcm.plaintext_request(registration_id=gcm_ID, data=data2)
    print 'sent GCM for ' + str(gcm_ID)
    print response


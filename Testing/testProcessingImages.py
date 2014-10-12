__author__ = 'michaelluo'

import unittest

from S3.S3 import uploadImageToS3Bucket
import json, httplib


class TestSequenceFunctions(unittest.TestCase):

    def test_upload(self):
        # make sure the shuffled sequence does not lose any elements
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        #params = 'hello'
        #data = urllib.urlencode({'test': 'Status'})
        data = json.dumps({'test': 'Status'})
        print str(data)
        conn = httplib.HTTPConnection("54.85.9.56")

    # def test_getImages(self):


if __name__ == '__main__':
    unittest.main()


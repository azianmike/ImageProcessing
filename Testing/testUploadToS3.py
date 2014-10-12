__author__ = 'michaelluo'

import unittest
import os
from S3.S3 import uploadListOfImagesToS3, deleteImageKeys
from S3.CompressAndSaveImages import compressAndSaveImages

# def test_getImages(self):
def cleanUsdfp(urlsAndKeys):
    for urlAndKey in urlsAndKeys:
        os.remove(urlAndKey[0])

class TestUploadToS3(unittest.TestCase):

    def test_upload(self):
        # make sure the shuffled sequence does not lose any elements
        url = uploadListOfImagesToS3(['testImages/Screen Shot 2014-10-08 at 5.35.21 PM.png'])
        self.assertIsNotNone(url)
        self.assertEquals(url[0][0],'testImages/Screen Shot 2014-10-08 at 5.35.21 PM.png')
        deleteImageKeys([url[0][0]])

        url = uploadListOfImagesToS3(['testImages/Screen Shot 2014-10-08 at 12.20.12 AM.png'])
        self.assertIsNotNone(url)
        self.assertEquals(url[0][0],'testImages/Screen Shot 2014-10-08 at 12.20.12 AM.png')
        deleteImageKeys([url[0][0]])



    def test_compressAndUpload(self):
        urlsAndKey = compressAndSaveImages('testImages/')
        print urlsAndKey
        self.assertEquals(len(urlsAndKey), 6)
        cleanUsdfp(urlsAndKey)
        imageKeys = []
        for key in urlsAndKey:
            imageKeys.append(key[0])
        deleteImageKeys(imageKeys)



if __name__ == '__main__':
    unittest.main()


__author__ = 'michaelluo'

from boto.s3.connection import S3Connection
from boto.s3.key import Key
import apikeys

def uploadImageToS3Bucket(bucket, imageName):
    '''
    The username will be the folder that the image is saved in

    '''

    k = Key(bucket)
    k.key = imageName
    k.set_contents_from_filename(imageName, None, None)
    k.set_acl('public-read')
    url = k.generate_url(expires_in=0,query_auth=False)
    returnKey = k.key
    return (returnKey,url)


def getImagesFromS3():
    conn = S3Connection(apikeys.AWSAccessKeyId, apikeys.AWSSecretAccessKey)
    perphektBucket = conn.get_bucket('perphekt.images', False, None)

    for key in perphektBucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )


def uploadListOfImagesToS3(listOfPaths):
    '''
    The username will be the folder that the image is saved in

    '''
    conn = S3Connection(apikeys.AWSAccessKeyId, apikeys.AWSSecretAccessKey)
    perphektBucket = conn.get_bucket('perphekt.images', False, None)

    urlAndKeys = []
    for path in listOfPaths:
        urlAndKeys.append(uploadImageToS3Bucket(perphektBucket,path))

    conn.close()
    return urlAndKeys

def deleteImageKeys(imageKeys):
    conn = S3Connection(apikeys.AWSAccessKeyId, apikeys.AWSSecretAccessKey)
    perphektBucket = conn.get_bucket('perphekt.images', False, None)

    for imageKey in imageKeys:
        deleteImageFromBucket(perphektBucket, imageKey)


def deleteImageFromBucket(bucket, imageKey):
    bucket.delete_key(imageKey)





__author__ = 'michaelluo'

from boto.s3.connection import S3Connection
from boto.s3.key import Key
import apikeys

def uploadImageToS3(pathToImage, imageName, userName):
    '''
    The username will be the folder that the image is saved in

    '''
    conn = S3Connection(apikeys.AWSAccessKeyId, apikeys.AWSSecretAccessKey)
    perphektBucket = conn.get_bucket('perphekt.images', False, None)

    k = Key(perphektBucket)
    k.key = userName + '/'+imageName
    k.set_contents_from_filename(pathToImage, None, None)
    k.set_acl('public-read')
    url = k.generate_url(expires_in=0,query_auth=False)
    conn.close()
    return url







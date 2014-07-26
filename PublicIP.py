__author__ = 'michaelluo'

import urllib2

def getPublicIP():
    pub_ip = urllib2.urlopen("http://169.254.169.254/latest/meta-data/public-ipv4").read()
    return pub_ip
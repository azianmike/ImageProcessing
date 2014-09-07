__author__ = 'michaelluo'

import httplib, urllib, json
import ImageCompareFolder

headers = {"Content-type": "application/json", "Accept": "text/plain"}
#params = 'hello'
#data = urllib.urlencode({'test': 'Status'})
data = json.dumps({'test': 'Status'})
print str(data)
conn = httplib.HTTPConnection("54.85.9.56")
#conn.request("GET", "/testPOST/")
conn.request("POST", "/testPOST/", str(data), headers)
res = conn.getresponse()
data = res.read()
print res.status
print data



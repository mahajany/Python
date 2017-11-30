#Used to make requests
import sys
import json
import urllib.request
URL=sys.argv[1]
print(sys.argv[0], "---->", sys.argv[1])
####print(x.read())
####x = urllib.request.urlopen('http://www.jsontest.com/')
x = json.load(urllib.request.urlopen(URL))
print(x)

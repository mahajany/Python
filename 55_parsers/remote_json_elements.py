#Used to make requests
import sys
import json
import urllib.request
URL=URL="https://jsonplaceholder.typicode.com/posts"
posts= json.load(urllib.request.urlopen(URL))
print("type(posts):", type(posts), ", len(posts):", len(posts))
post1=posts[0]
print("type(post1):", type(post1), ", len(post1):", len(post1))
for key, value in post1.items():
   print("Key:", key, "\t\tValue:", value)

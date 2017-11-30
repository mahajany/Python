from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
##MONGODB_URL="""localhost:27017/blog"""
MONGODB_URL="""mongodb://localhost:27017/blog"""
client = MongoClient(MONGODB_URL)
db=client.blog
collection_posts=db.posts
##
doc=collection_posts.find_one()
####################pprint(doc)
##
doc=collection_posts.find_one({"title":"Declaration of Independence"})
##pprint(doc)
##
doc=collection_posts.find_one({"title":"Declaration of Independence"},{"author":1,"permalink":1})
pprint(doc)
##
doc=collection_posts.find_one({"title":"Declaration of Independence"},{"author":1,"permalink":1,"_id":0})
pprint(doc)


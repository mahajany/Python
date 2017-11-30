import pymongo
import pprint
import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['test-database']
collection = db['test-collection']
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
pprint.pprint(posts.find_one())
pprint.pprint(posts.find_one({"author": "Eliot"}))
pprint.pprint(posts.find_one({"_id": post_id}))
document = client.db.collection.find_one({'_id': ObjectId(post_id)})
print(str(document))
print(posts.count())

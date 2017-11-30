from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId

# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
##MONGODB_URL="""localhost:27017/blog"""
MONGODB_URL="""mongodb://localhost:27017/blog"""
client = MongoClient(MONGODB_URL)
db=client.blog
collection_posts=db.posts
##
newPost = {"author": "Mike",
         "body": "My first blog post!",
         "title": "First blog post!",
         "permalink": "my-first-blog-post",
         "tags": ["mongodb", "python", "pymongo"],
         "comments": [{"body":"Wow...good", "email":"test@.detest.com", "author":"anonymous"}],
         "date": datetime.datetime.utcnow()}
##
new_post_id=collection_posts.insert_one(newPost).inserted_id
if new_post_id:
   print("Sucessfully inserted!", new_post_id)

the_post=collection_posts.find_one({"_id":ObjectId(new_post_id)})
pprint(the_post)
result=collection_posts.update_one({"_id":ObjectId(new_post_id)},
                                   {"$set": {"body":"No...I've written earlier as well, so it is second. Thanks."}}
                                  )
print("Updated ", result.matched_count, "posts.")
# 
result=collection_posts.delete_many({"permalink":"my-first-blog-post"})
print("Deleted ", result.deleted_count, "posts.")

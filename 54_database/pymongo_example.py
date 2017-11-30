from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
##MONGODB_URL="""localhost:27017/blog"""
MONGODB_URL="""mongodb://localhost:27017/blog"""
client = MongoClient(MONGODB_URL)
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
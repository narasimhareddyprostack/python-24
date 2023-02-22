import pymongo

#create monogo connection
client = pymongo.MongoClient()

#create Mongo database
mdb = client['prostackOne']

#create collection
mcol = mdb['emp']

mcol.insert_one({"id":101, "name":"Rahul"})
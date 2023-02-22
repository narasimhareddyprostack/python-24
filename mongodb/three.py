import pymongo

client = pymongo.MongoClient()

mdb = client['prostackOne']

mcol = mdb['emp']

for doc in mcol.find():
    print(type(doc))
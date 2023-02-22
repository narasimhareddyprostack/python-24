import pymongo

client = pymongo.MongoClient()

mdb = client['prostackOne']

mcol = mdb['emp']

for doc in mcol.find({"Sal":55000}):
    print(doc)
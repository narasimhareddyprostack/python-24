import pymongo

#create monogo connection
client = pymongo.MongoClient()

#create Mongo database
mdb = client['prostackOne']

#create collection
mcol = mdb['emp']

#Insert many records

mcol.insert_many([{"id":101, "name":"Rahul Gandhi","Sal":45000},{"id":102, "name":"Sonia Gandhi","Sal":55000},{"id":103, "name":"Priynka Gandhi","Sal":65000}])


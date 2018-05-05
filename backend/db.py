import pymongo

def connect_mongodb(DB_HOSTMONGODB,DB_MONGODB):
    client = pymongo.MongoClient(DB_HOSTMONGODB)
    return client[DB_MONGODB]

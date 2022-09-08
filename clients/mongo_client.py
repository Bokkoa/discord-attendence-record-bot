import os
import pymongo

MONGO_HOST = os.getenv('MONGO_HOST', None);
MONGO_DB = os.getenv('MONGO_DB', None);
MONGO_COLLECTION = "attendence_record"

client = pymongo.MongoClient(MONGO_HOST)
db = client[MONGO_DB]
collection =  db[MONGO_COLLECTION]

def insert_attendence(*args):
    document = {
        "name": args[0],
        "date": args[1],
        "type": args[2]
    }
    collection.insert_one(document)

from pymongo import MongoClient
import datetime
from stdiocolours import OKGREEN, ENDC, OKBLUE

class Mongo:
    def __init__(self, conn, db_name, collection_name): 
        self.client = MongoClient(conn)
        self.db_collection = self.client[db_name][collection_name]
  
    def insert_documents(self, data):
        for d in data:
            d['created_at'] = datetime.datetime.now()

        result = self.db_collection.insert_many(data)
        print(OKGREEN + '\nInserted %s documents'%(len(result.inserted_ids)) + ENDC+'\n')
        print(OKBLUE + 'Document ObjectIDs:\n\n%s'%(result.inserted_ids) + ENDC+'\n')
        print(OKGREEN + 'Done' + ENDC+'\n')
        self.client.close()
        return result.inserted_ids
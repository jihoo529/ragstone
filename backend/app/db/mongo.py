import pymongo
from pymongo.errors import PyMongoError

class MongoKeyValueDB:
    def __init__(self, db_name='ragstone', collection_name='populated_files', uri='mongodb://mongodb:27017/'):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def set(self, key, ibx, is_populated):
        try:
            self.collection.update_one(
                {'_id': key},
                {'$set': {'ibx': ibx, 'is_populated': is_populated}},
                upsert=True
            )
        except PyMongoError as e:
            print(f"Error setting value: {e}")

    def get(self, key):
        try:
            result = self.collection.find_one({'_id': key})
            return result if result else None
        except PyMongoError as e:
            print(f"Error getting value: {e}")
            return None

    def delete(self, key):
        try:
            self.collection.delete_one({'_id': key})
        except PyMongoError as e:
            print(f"Error deleting key: {e}")

    def keys(self):
        try:
            return [doc['_id'] for doc in self.collection.find()]
        except PyMongoError as e:
            print(f"Error retrieving keys: {e}")
            return []

    def values(self):
        try:
            return [{'ibx': doc['ibx'], 'is_populated': doc['is_populated']} for doc in self.collection.find()]
        except PyMongoError as e:
            print(f"Error retrieving values: {e}")
            return []

    def items(self):
        try:
            return [(doc['_id'], {'ibx': doc['ibx'], 'is_populated': doc['is_populated']}) for doc in self.collection.find()]
        except PyMongoError as e:
            print(f"Error retrieving items: {e}")
            return []

    def clear(self):
        try:
            self.collection.delete_many({})
        except PyMongoError as e:
            print(f"Error clearing database: {e}")

    def clear_with_val(self, val):
        try:
            self.collection.delete_many({'ibx': val})
        except PyMongoError as e:
            print(f"Error clearing database: {e}")

    def close(self):
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
import pymongo
class DataLoader:
    def __init__(self):

        self.db_url = ''
        self.database_name = 'mydatabase'
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = client[self.database_name]

    def insert(self, object_to_save):
        pass

    def find(self, keys: list):
        pass

    def remove(self, keys):
        pass

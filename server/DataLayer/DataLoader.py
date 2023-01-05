import pymongo

from server.Tools.SystemConfig import SystemConfig


class DataLoader:
    def __init__(self):

        self.db_url = ''
        self.database_name = SystemConfig().DB_NAME
        self.cluster = pymongo.MongoClient(SystemConfig().MONGO_URI)
        self.db = self.cluster[self.database_name]

    def insert(self, object_to_save):
        pass

    def find(self, keys: list):
        pass

    def remove(self, keys):
        pass

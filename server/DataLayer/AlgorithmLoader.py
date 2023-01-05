from server.DataLayer.AlgorithmDto import AlgorithmDto
from server.DataLayer.DataLoader import DataLoader


class AlgorithmLoader(DataLoader):

    def __init__(self):
        super().__init__()
        self.collection_name = 'Algorithms'
        self.collection = self.db[self.collection_name]

    def insert(self, object_to_save: AlgorithmDto):
        # TODO validate does not exist in DB
        self.collection.insert_one(object_to_save)

    def find(self, keys):
        result = self.collection.find_one({"file": keys})
        print(result)

    def remove(self, keys):
        super().remove(keys)

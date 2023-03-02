from server.DataLayer.AlgorithmDto import AlgorithmDto
from server.DataLayer.DataLoader import DataLoader
import json


class AlgorithmLoader(DataLoader):

    def __init__(self):
        super().__init__()
        self.collection_name = 'Algorithms'
        self.collection = self.db[self.collection_name]

    def insert(self, object_to_save: AlgorithmDto):
        # TODO validate does not exist in DB
        obj_json = json.dumps(object_to_save, default=lambda x: x.__dict__)
        self.collection.insert_one(obj_json)

    def find(self, algo_name):
        result = self.collection.find_one({"name": algo_name})
        return result['file_content']

    def remove(self, keys):
        super().remove(keys)

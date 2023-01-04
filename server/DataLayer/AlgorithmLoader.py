from server.DataLayer.AlgorithmDto import AlgorithmDto
from server.DataLayer.DataLoader import DataLoader


class AlgorithmLoader(DataLoader):

    def __init__(self):
        super().__init__()
        self.collection_name = 'Algorithms'
        self.collection = self.db[self.collection_name]

    def insert(self, object_to_save: AlgorithmDto):
        file_content = open(object_to_save.file, "r").read()
        document = {"filename": object_to_save.name, "file": file_content, "args_list": object_to_save.args_lst}
        self.collection.insert_one(document)

    def find(self, keys):
        result = self.collection.find_one({"file": keys})
        print(result)

    def remove(self, keys):
        super().remove(keys)

from server.DataLayer.AlgorithmDto import AlgorithmDto
from server.DataLayer.DataLoader import DataLoader


class AlgorithmLoader(DataLoader):

    def __init__(self):
        super().__init__()
        self.collection_name = 'Algorithms'
        self.collection = self.db[self.collection_name]

    def insert(self, object_to_save: AlgorithmDto):
        # TODO validate does not exist in DB
        obj_json = {
            "name": object_to_save.name,
            "file_content": object_to_save.file_content,
            "description": object_to_save.description,
            "argument_lst": [],
            "additional_info": object_to_save.additional_info,
            "output_example": object_to_save.output_example
        }
        self.collection.insert_one(obj_json)

    def find(self, algo_name):
        result = self.collection.find_one({"name": algo_name})
        return result['file_content']

    def remove(self, keys):
        query = {"name": keys}
        result = self.collection.delete_one(query)
        return result

    def get_all_algorithms(self):
        result = self.collection.find({"name": {"$ne": None}})
        return result

    def update(self, algo_dto):

        obj_json = {
            "name": algo_dto.name,
            "file_content": algo_dto.file_content,
            "description": algo_dto.description,
            "argument_lst": [],
            "additional_info": algo_dto.additional_info,
            "output_example": algo_dto.output_example
        }
        query = {"name":algo_dto.name}
        self.collection.update_one(query,{"$set": obj_json})

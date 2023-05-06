import json

from server.DataLayer.AlgorithmDto import AlgorithmDto
import pymongo
from pymongo import MongoClient

# from server.Tools.Logger import Logger
from server.Tools.SystemConfig import SystemConfig
from server.DataLayer.ArgumentDescriptionDto import ArgumentDescriptionDto



class AlgorithmLoader:

    def __init__(self):
        self.database_name = SystemConfig().DB_NAME
        self.cluster = MongoClient(SystemConfig().MONGO_URI)
        self.db = self.cluster[self.database_name]
        self.collection_name = 'Algorithms'
        self.collection = self.db[self.collection_name]

    def insert(self, object_to_save: AlgorithmDto):
        # TODO validate does not exist in DB
        serializedArgumentList = [arg.serialize() for arg in object_to_save.argument_lst]
        obj_json = {
            "name": object_to_save.name,
            "file_content": object_to_save.file_content,
            "description": object_to_save.description,
            "argument_lst": json.dumps(serializedArgumentList),
            "additional_info": object_to_save.additional_info,
            "output_example": object_to_save.output_example
        }
        self.collection.insert_one(obj_json)

    def find(self, algo_name):
        result = self.collection.find_one({"name": algo_name})
        if result is None:
            return result
        return result['file_content']

    def remove(self,algo_name):
        query = {'name': algo_name}
        self.collection.delete_one(query)
        # Logger().debug(f'removed {name} from DB')

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

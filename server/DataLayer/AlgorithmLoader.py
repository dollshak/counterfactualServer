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
            "output_example": object_to_save.output_example,
            "algo_type": object_to_save.algo_type
        }
        self.collection.insert_one(obj_json)

    def find_many(self, algo_names):
        algos = []
        query = {"name": {"$in": algo_names}}
        result = self.collection.find(query)
        if result is None:
            return []
        for data_obj in result:
            content_ = data_obj['file_content']
            name_ = data_obj['name']
            description_ = data_obj['description']
            additional_info_ = data_obj['additional_info']
            output_example_ = data_obj['output_example']
            argument_lst_ = json.loads(data_obj['argument_lst'])
            algo_type_ = data_obj['algo_type']
            arg_list = []
            if argument_lst_ is not None:
                arg_list = [ArgumentDescriptionDto(arg['param_name'], arg['description'],  arg['accepted_types']) for arg in argument_lst_]
            algo = AlgorithmDto(content_,name_, arg_list, description_,additional_info_,output_example_,algo_type_ )
            algos.append(algo)
        return algos

    def find(self, algo_name):
        result = self.collection.find_one({"name": algo_name})
        if result is None:
            return result
        return result

    def remove(self, algo_name):
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
        query = {"name": algo_dto.name}
        self.collection.update_one(query, {"$set": obj_json})

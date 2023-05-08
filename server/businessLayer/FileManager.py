import os
import json
from server.DataLayer.AlgorithmDto import AlgorithmDto
from server.DataLayer.AlgorithmLoader import AlgorithmLoader
from server.DataLayer.ArgumentDescriptionDto import ArgumentDescriptionDto
from server.businessLayer.Algorithms.Algorithm import Algorithm
# from server.Tools.Logger import Logger
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription


class FileManager:
    def __init__(self, config=SystemConfig()):
        self.config = config

    def add_algorithm(self, file_content, cf_desc: CounterFactualAlgorithmDescription):
        """

          add algorithm to DB and to folder, validates file name does not exist
           Parameters
           ----------
           file_content : str
               The name of the animal
           cf_desc : CounterFactualAlgorithmDescription
                The CF

       """
        if not self.is_algo_exist_in_db(cf_desc.name):
            decoded = self.content_to_file(file_content, cf_desc.name)
            print("before save in db")
            self.save_in_db(decoded, cf_desc)
        else:
            raise FileExistsError()

    def content_to_file(self, content, file_name):
        """
        receives a file string and convert it to a file
        """
        # TODO create generic implementation for various content types
        full_path = self.config.ALGORITHMS_DIR_PATH + "/" + file_name + ".py"
        with open(full_path, 'w') as f:
            if not isinstance(content, str):
                content = content.decode('utf-8')
            f.write(content)
        return content

    def save_in_db(self, file_content, cf_desc: CounterFactualAlgorithmDescription):
        loader = AlgorithmLoader()
        args_dtos = [ArgumentDescriptionDto(arg.param_name, arg.description, arg.accepted_types) for arg in
                     cf_desc.argument_lst]
        algo_dto = AlgorithmDto(file_content, cf_desc.name, args_dtos, cf_desc.description, cf_desc.additional_info,
                                cf_desc.output_example, cf_desc.algo_type)

        loader.insert(algo_dto)
        print("after insert to db")

    def remove_algo(self, algo_name):
        if self.is_algo_exist_in_db(algo_name):
            self.remove_from_db(algo_name)
        #     TODO use logger
        if (self.is_algo_exist_in_system(algo_name)):
            self.remove_algo_system(algo_name)
        #     TODO use logger here
        if self.is_algo_exist_in_db(algo_name):
            return False
            #     TODO use logger here
        if self.is_algo_exist_in_system(algo_name):
            return False
            #     TODO use logger here
        return True

    def remove_algo_system(self, algo_name):
        # TODO need to change hard coded .py
        full_path = self.config.ALGORITHMS_DIR_PATH + "/" + algo_name + ".py"
        os.remove(full_path)

    def remove_from_db(self, algo_name: str):
        loader = AlgorithmLoader()
        loader.remove(algo_name)

    def is_algo_exist_in_system(self, name: str):
        """
        :param name: file name without the file type (such as '.py'
        :return: true if the file is in the algo directory
        """
        # TODO need to change hard coded .py
        return name + '.py' in os.listdir(self.config.ALGORITHMS_DIR_PATH)

    def is_algo_exist_in_db(self, name: str):
        loader = AlgorithmLoader()
        result = loader.find(name)
        return result is not None and len(result) > 0

    def load_algorithm(self, file_name):
        result = AlgorithmLoader().find(file_name)
        return result

    def load_algorithms(self, algorithms_names: list[str]):
        """
        loads algorithms from DB if needed (not in folder)
        :param algorithms_names:
        :return:
        """
        # TODO need to validate that deserialization here works well
        dto_algos = AlgorithmLoader().find_many(algorithms_names)
        if dto_algos is None:
            pass
        cf_descs = []
        for obj in dto_algos:
            self.content_to_file(obj.file_content, obj.param_name)
            args_list = [ArgumentDescription(arg.param_name, arg.description, arg.accepted_types) for arg
                         in obj.argument_lst]
            cf_descs.append(
                CounterFactualAlgorithmDescription(obj.param_name, args_list, obj.description, obj.additional_info,
                                                   obj.output_example, obj.algo_type))
        return cf_descs

    def get_all_algorithms(self):
        algos = AlgorithmLoader().get_all_algorithms()
        result = []
        for algo in algos:
            result.append(
                {"_id": str(algo['_id']), "name": algo['name'], "description": algo['description'], "argument_lst": json.loads(algo['argument_lst']),
                 "additional_info": algo['additional_info'], "output_example": algo['output_example']})
        return result

    def edit_algorithm(self, file_content, cf_desc):
        if self.is_algo_exist(cf_desc.param_name):
            decoded = self.content_to_file(file_content, cf_desc.param_name)
            self.updated_in_db(decoded, cf_desc)

    def updated_in_db(self, file_content, cf_desc):
        loader = AlgorithmLoader()
        args_dtos = [ArgumentDescriptionDto(arg.param_name, arg.description, arg.accepted_types) for arg in
                     cf_desc.argument_lst]
        algo_dto = AlgorithmDto(file_content, cf_desc.param_name, args_dtos, cf_desc.description, cf_desc.additional_info,
                                cf_desc.output_example,cf_desc.param_name)

        loader.update(algo_dto)

    def remove_algorithm(self, algortihm_name):
        loader = AlgorithmLoader()
        if self.is_algo_exist(algortihm_name):
            return loader.remove(algortihm_name)

    def get_files_names_and_import_from_db(self, algo_names):
        self.import_missing_algorithms(algo_names)
        # TODO need to remove hard coded .py
        return [name + '.py' for name in algo_names]

    def import_missing_algorithms(self, algo_names):
        missing_algos = []
        for name in algo_names:
            # TODO need to change from hard coded .py
            file_name = name
            if not self.is_algo_exist_in_system(file_name):
                missing_algos.append(name)
        if len(missing_algos) > 0:
            # TODO add logger -> importing ...
            self.load_algorithms(missing_algos)
#         TODO create logger all algorithms imported

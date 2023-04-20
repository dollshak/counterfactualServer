import os

from server.DataLayer.AlgorithmDto import AlgorithmDto
from server.DataLayer.AlgorithmLoader import AlgorithmLoader
from server.DataLayer.ArgumentDescriptionDto import ArgumentDescriptionDto
from server.businessLayer.Algorithms.Algorithm import Algorithm
from server.Tools.Logger import Logger
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription


class FileManager:
    def __init__(self):
        self.config = SystemConfig()
        self.logger = Logger()

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
        if not self.is_algo_exist(cf_desc.name):
            decoded = self.content_to_file(file_content, cf_desc.name)
            self.save_in_db(decoded, cf_desc)

    def content_to_file(self, content, file_name):
        """
        receives a file string and convert it to a file
        """
        # TODO create generic implementation for various content types
        full_path = SystemConfig().ALGORITHMS_DIR_PATH + "/" + file_name + ".py"
        with open(full_path, 'w') as f:
            decoded = content.decode('utf-8')
            f.write(decoded)
        return decoded

    def save_in_db(self, file_content, cf_desc: CounterFactualAlgorithmDescription):
        loader = AlgorithmLoader()
        args_dtos = [ArgumentDescriptionDto(arg.param_name, arg.description, arg.accepted_types) for arg in
                     cf_desc.argument_lst]
        algo_dto = AlgorithmDto(file_content, cf_desc.name, args_dtos, cf_desc.description, cf_desc.additional_info,
                                cf_desc.output_example)

        loader.insert(algo_dto)

    def is_algo_exist(self, name: str):
        return name in os.listdir(SystemConfig().ALGORITHMS_DIR_PATH)

    def load_algorithm(self, file_name):
        result = AlgorithmLoader().find(file_name)
        return result

    def load_algorithms(self, files_names: list[str]):
        """
        loads algorithms from DB if needed (not in folder)
        :param files_names:
        :return:
        """
        objects_from_db: list[AlgorithmDto] = [AlgorithmLoader().find([name]) for name in files_names]
        cf_descs = []
        for obj in objects_from_db:
            self.content_to_file(obj.file_content, obj.name)
            args_list = [ArgumentDescription(arg.name, arg.description, arg.accepted_types) for arg in obj.argument_lst]
            cf_descs.append(
                CounterFactualAlgorithmDescription(obj.name, args_list, obj.description, obj.additional_info,
                                                   obj.output_example))
        return cf_descs

    def get_all_algorithms(self):
        algos = AlgorithmLoader().get_all_algorithms()
        result = []
        for algo in algos:
            result.append(
                {"name": algo['name'], "description": algo['description'], "argument_lst": algo['argument_lst'],
                 "additional_info": algo['additional_info'], "output_example": algo['output_example']})
        return result

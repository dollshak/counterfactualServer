from server.businessLayer.Algorithms.Algorithm import Algorithm
from server.Tools.Logger import Logger
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription


class AlgorithmManager:
    def __init__(self, config: SystemConfig):
        self.logger = Logger(config)

    def create_algorithm(self, cf_algo: CounterFactualAlgorithmDescription, file_content):
        # TODO save in mongo
        raise Exception("Not implemented")

    def is_algo_exist(self, name: str):
        raise Exception("Not implemented")

    def get_all_algo_names(self):
        raise Exception("Not implemented")

    def get_algorithm(self, name: str):
        raise Exception("Not implemented")

    def remove_algorithm(self, name: str):
        raise Exception("Not implemented")

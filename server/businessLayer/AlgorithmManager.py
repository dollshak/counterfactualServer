from server.businessLayer.Algorithm import Algorithm
from server.businessLayer.Logger import Logger
from server.businessLayer.SystemConfig import SystemConfig


class AlgorithmManager:
    def __init__(self, config: SystemConfig):
        self.logger = Logger(config)

    def create_algorithm(self, CF_algo: Algorithm):
        raise Exception("Not implemented")

    def is_algo_exist(self, name: str):
        raise Exception("Not implemented")

    def get_all_algo_names(self):
        raise Exception("Not implemented")

    def get_algorithm(self, name: str):
        raise Exception("Not implemented")

    def remove_algorithm(self, name: str):
        raise Exception("Not implemented")


from server.businessLayer.SystemConfig import SystemConfig
from server.businessLayer.Engine import Engine
from server.businessLayer.Logger import Logger


class AlgorithmsController:
    def __init__(self,config:SystemConfig):
        self.algorithms_lst = list()
        self.engine = Engine()
        self.logger = Logger(config)

    def get_algorithm(self, name):
        raise Exception("Not implemented.")

    def get_all_algorithms(self):
        raise Exception("Not implemented.")

    def add_new_algorithm(self):
        raise Exception("Not implemented.")

    def remove_algorithm(self, algorithm):
        raise Exception("Not implemented.")

    def run_selected_algorithms(self):
        raise Exception("Not implemented.")

    def load_algorithms(self):
        raise Exception("Not implemented.")

    def edit_algorithm(self, algorithm):
        raise Exception("Not implemented.")

    def handle_output(self,outputs:list):
        raise Exception("Not implemented")

    def handle_input(self,inputs:list):
        raise Exception("Not implemented")
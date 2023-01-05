from server.DataLayer.AlgorithmLoader import AlgorithmLoader
from server.businessLayer.Algorithms.Algorithm import Algorithm
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Engine.EnginePY import EnginePY
from server.Tools.Logger import Logger


class AlgorithmsController:
    def __init__(self,config:SystemConfig):
        self.algorithms_lst = list()
        self.engine = EnginePY()
        self.logger = Logger(config)

    def get_algorithm(self, name):
        raise Exception("Not implemented.")

    def get_all_algorithms(self):
        raise Exception("Not implemented.")

    def add_new_algorithm(self, file , algorithmDTO: Algorithm):
        loader = AlgorithmLoader()
        loader.insert(algorithmDTO)

    def remove_algorithm(self, algorithm):
        raise Exception("Not implemented.")

    def run_selected_algorithms(self, filename, model,cf_args,inputs):
        loader = AlgorithmLoader()
        algo = loader.find(filename)
        # TODO save in dir
        self.engine.run_algorithm(model,filename,cf_args,inputs)

    def load_algorithms(self):
        raise Exception("Not implemented.")

    def edit_algorithm(self, algorithm):
        raise Exception("Not implemented.")

    def handle_output(self,outputs:list):
        raise Exception("Not implemented")

    def handle_input(self,inputs:list):
        raise Exception("Not implemented")
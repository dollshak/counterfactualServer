from server.DataLayer.AlgorithmLoader import AlgorithmLoader
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Engine.EngineController import EngineController
from server.businessLayer.FileManager import FileManager
from server.businessLayer.Algorithms.Algorithm import Algorithm
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.Engine.EnginePY import EnginePY
from server.Tools.Logger import Logger
from server.businessLayer.ML_Models.MlModel import MlModel


class AlgorithmsController:
    def __init__(self, ):
        self.algorithms_lst = list()
        self.logger = Logger()
        self.file_manager = FileManager()

    def get_algorithm(self, name):
        return self.file_manager.load_algorithm(name)

    def get_all_algorithms(self):
        return self.file_manager.get_all_algorithms()

    def add_new_algorithm(self, file_content, name: str, argument_lst: list[dict], description: str,
                          additional_info: str,
                          output_example: list[str]):
        args_lst = [ArgumentDescription(param_name=arg['param_name'], description=arg['description'],
                                        accepted_types=arg['accepted_types']) for arg in argument_lst]
        cf_desc = CounterFactualAlgorithmDescription(name, args_lst, description, additional_info, output_example)
        self.file_manager.add_algorithm(file_content, cf_desc)
        self.algorithms_lst.append(cf_desc)

    def remove_algorithm(self, algorithm):
        raise Exception("Not implemented.")

    def run_selected_algorithms(self, algo_names: list[str], algo_param_list: list[list], model: MlModel,
                                model_input: list, feature_names):
        # self.file_manager.load_algorithms(algo_names)
        engine_controller = EngineController()
        return engine_controller.run_algorithms(algo_names, model, model_input, algo_param_list )

    def edit_algorithm(self, algorithm):
        raise Exception("Not implemented.")

    def handle_output(self, outputs: list):
        raise Exception("Not implemented")

    def handle_input(self, inputs: list):
        raise Exception("Not implemented")

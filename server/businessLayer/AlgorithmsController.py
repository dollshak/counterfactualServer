from server.DataLayer.AlgorithmLoader import AlgorithmLoader
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Engine.EngineController import EngineController
from server.businessLayer.FileManager import FileManager
from server.businessLayer.Algorithms.Algorithm import Algorithm
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.Engine.EnginePY import EnginePY
from server.businessLayer.ML_Models.MlModel import MlModel
from server.Tools.Logger import Logger

logger = Logger()


class AlgorithmsController:
    def __init__(self, config=SystemConfig()):
        self.config = config
        # self.logger = Logger()
        self.file_manager = FileManager(config)

    def get_algorithm(self, name):
        return self.file_manager.load_algorithm(name)

    def get_all_algorithms(self):
        return self.file_manager.get_all_algorithms()

    def add_new_algorithm(self, file_content, name: str, argument_lst: list[dict], description: str,
                          additional_info: str,
                          output_example: list[str],
                          type: list[str]):
        args_lst = [ArgumentDescription(param_name=arg['param_name'], description=arg['description'],
                                        accepted_types=arg['accepted_types'] ) for arg in argument_lst]
        cf_desc = CounterFactualAlgorithmDescription(name, args_lst, description, additional_info, output_example, type)
        self.file_manager.add_algorithm(file_content, cf_desc)

    def remove_algorithm(self, algorithm_name):
        self.file_manager.remove_algorithm(algorithm_name)
        logger.debug(f'The algorithm {algorithm_name} has been removed.')

    def run_selected_algorithms(self, algo_names: list[str], algo_param_list: list[list], model: MlModel,
                                model_input: list, feature_names):
        # self.file_manager.load_algorithms(algo_names)
        engine_controller = EngineController()
        Logger().debug("importing file names from db")
        algo_names = self.file_manager.get_files_names_and_import_from_db(algo_names)
        return engine_controller.run_algorithms(algo_names, model, model_input, algo_param_list)

    def edit_algorithm(self, file_content, name: str, argument_lst: list[dict], description: str,
                       additional_info: str,
                       output_example: list[str],
                       algo_type):
        # TODO check this method until algorithmLoader
        args_lst = [ArgumentDescription(param_name=arg['param_name'], description=arg['description'],
                                        accepted_types=arg['accepted_types']) for arg in argument_lst]
        cf_desc = CounterFactualAlgorithmDescription(name, args_lst, description, additional_info, output_example,
                                                     algo_type)
        self.file_manager.edit_algorithm(file_content, cf_desc)
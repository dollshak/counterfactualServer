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
import collections

logger = Logger()


class AlgorithmsController:
    def __init__(self, config):
        self.config = config
        self.file_manager = FileManager(config)

    def get_algorithm(self, name):
        return self.file_manager.load_algorithm(name)

    def get_all_algorithms(self):
        return self.file_manager.get_all_algorithms()

    def add_new_algorithm(self, file_content, name: str, argument_lst: list[dict], description: str,
                          additional_info: str,
                          output_example: list[str],
                          type: list[str]):
        if not isinstance(type, list):
            logger.error(f'Trying to add algorithm: {name} - the algo type field got a non list value')
            raise TypeError("Algo type needs to be in the shape of list")
        type = [x.lower() for x in type]
        if 'regressor' not in type and 'classifier' not in type:
            logger.error(f'Trying to add algorithm: {name} - the algo type field is not classifier or regressor')
            raise ValueError("Algo type needs to be regressor or classifier")
        args_lst = [ArgumentDescription(param_name=arg['param_name'], description=arg['description'],
                                        accepted_types=arg['accepted_types'], default_value=arg['default_value']
                                        if 'default_value' in arg.keys() else None) for arg in argument_lst]
        params = []
        for arg in args_lst:
            p_name = arg.param_name
            if p_name == "":
                logger.error(f'Trying to add the algorithm {name} but one of the arguments name is empty')
                raise ValueError("All params has to have a name and can't be empty string")

            params.append(p_name)
        dup_params = [item for item, count in collections.Counter(params).items() if count > 1]
        if len(dup_params) > 0:
            logger.error(f'Trying to add the algorithm {name} but there are several params with non unique name.')
            raise ValueError("Cant add two or more arguments with the same name")
        cf_desc = CounterFactualAlgorithmDescription(name, args_lst, description, additional_info, output_example, type)
        self.file_manager.add_algorithm(file_content, cf_desc)

    def remove_algorithm(self, algorithm_name):
        self.file_manager.remove_algorithm(algorithm_name)
        logger.debug(f'The algorithm {algorithm_name} has been removed.')

    def run_selected_algorithms(self, algo_names: list[str], algo_param_list: list[list], model: MlModel,
                                model_input: list,feature_names):
        # self.file_manager.load_algorithms(algo_names)
        engine_controller = EngineController(self.config)
        Logger().debug("importing file names from db")
        algo_names = self.file_manager.get_files_names_and_import_from_db(algo_names)
        return engine_controller.run_algorithms(algo_names, model, model_input, algo_param_list)

    def edit_algorithm(self, file_content, name: str, argument_lst: list[dict], description: str,
                       additional_info: str,
                       output_example: list[str],
                       algo_type, origin_algo_name):
        if not isinstance(algo_type, list):
            logger.error(f'In edit algorithm for {origin_algo_name} - the algo type field got a non list value')
            raise TypeError("Algo type needs to be in the shape of list")
        if 'regressor' not in algo_type and 'classifier' not in algo_type:
            logger.error(
                f'In edit algorithm for {origin_algo_name} - the algo type field is not classifier or regressor')
            raise ValueError("Algo type needs to be regressor or classifier")
        args_lst = [ArgumentDescription(param_name=arg['param_name'], description=arg['description'],
                                        accepted_types=arg['accepted_types'], default_value=arg['default_value']) for
                    arg in argument_lst]
        cf_desc = CounterFactualAlgorithmDescription(name, args_lst, description, additional_info, output_example,
                                                     algo_type)
        self.file_manager.edit_algorithm(file_content, cf_desc, origin_algo_name)

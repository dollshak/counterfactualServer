import os
import importlib
from types import ModuleType

from server.Tools.FailedCFException import FailedCFException
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.Engine.EngineAPI import EngineAPI
from server.businessLayer.FileManager import FileManager
from server.businessLayer.ML_Models.MlModel import MlModel
import json

class EnginePY(EngineAPI):

    def __init__(self, model, file_name, cf_params_list, config):
        super().__init__(model, file_name, cf_params_list, config)
        self.validate_arguments()

    # def __init__(self):
    #     super().__init__()
    #     self.selected_algo_lst = list()
    #     self.working_directory_path = os.getcwd()
    #     self.algos_path = 'server.businessLayer.CF_Algorithms.'

    def run_algorithm(self, model_input: list):
        name, suffix = os.path.splitext(self.file_name)
        module_path = SystemConfig().ALGORITHMS_DIR_PATH_MODULES + name
        cf_algo = self.import_cf_algo(module_path)
        results = cf_algo.explain(model_input)
        return results

    def import_cf_algo(self, module_path):
        try:
            algo_module = importlib.import_module(module_path)
            cf_algo = algo_module.initAlgo(self.model, self.cf_params)
        except:
            raise Exception(f'failed to import module {self.file_name}')
        return cf_algo

    def validate_arguments(self):
        file_manager = FileManager(self.config)
        name, suffix = os.path.splitext(self.file_name)

        algo_val = file_manager.get_algorithm(name)
        if algo_val is None or len(algo_val) == 0:
            raise FailedCFException(f'There is no CF algorithm named:{name}.py')
        arg_list = algo_val['argument_lst']
        arg_list = json.loads(arg_list)
        names = [arg['param_name'] for arg in arg_list]
        params = list(self.cf_params.keys())
        if len(names) < len(params):
            raise FailedCFException(f'too many arguments given for {name}')
        if len(names) > len(params):
            raise FailedCFException(f'not enough arguments given for {name}')
        for param_name in names:
            if param_name not in params:
                raise FailedCFException(f'{param_name} is missing for {name}')

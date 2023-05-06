import os
import importlib
from types import ModuleType

from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.Engine.EngineAPI import EngineAPI
from server.businessLayer.ML_Models.MlModel import MlModel

class EnginePY(EngineAPI):

    def __init__(self, model, file_name, cf_params_list):
        super().__init__(model, file_name, cf_params_list)

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
import os
import importlib
from types import ModuleType

from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.Engine.EngineAPI import EngineAPI
from server.businessLayer.ML_Models.MlModel import MlModel


class EnginePY(EngineAPI):
    def __init__(self):
        super().__init__()
        self.selected_algo_lst = list()
        self.working_directory_path = os.getcwd()
        self.algos_path = 'server.businessLayer.CF_Algorithms.'

    def run_algorithm(self, model: MlModel, algo_name: str, model_input: list, cf_inputs: list):
        module_path = self.algos_path + algo_name
        try:
            algo_module: ModuleType = importlib.import_module(module_path)
            cf_algo: CounterFactualAlgorithmDescription = algo_module.initAlgo(cf_name, args_desc, model)
        except:
            raise Exception(f'failed to import module {file_name}')

        results = cf_algo.explain(model_input)
        return results

    def run_algorithms(self, model, inputs: list):
        raise Exception("Not implemented.")

    def import_(self):
        raise Exception("Not implemented.")

    def create_exec(self, name):
        raise Exception("Not implemented.")

    def delete_exec(self, name):
        raise Exception("Not implemented.")

    def run_exec(self, name):
        raise Exception("Not implemented.")

    def run_model(self):
        raise Exception("Not implemented.")

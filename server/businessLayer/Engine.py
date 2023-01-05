import numbers
import os
import subprocess
import importlib
from types import ModuleType

from server.businessLayer.CounterFactualAlgorithm import CounterFactualAlgorithm
from server.businessLayer.Logger import Logger
from server.businessLayer.MlModel import MlModel


class Engine:
    def __init__(self):
        self.selected_algo_lst = list()
        self.working_directory_path = os.getcwd()
        self.algos_path = 'server.businessLayer.CF_Algorithms.'

    def run_algorithm(self, model: MlModel, file_name, cf_name, args_desc, model_input):
        module_path = self.algos_path + file_name
        try:
            algo_module: ModuleType = importlib.import_module(module_path)
            cf_algo: CounterFactualAlgorithm = algo_module.init(cf_name, args_desc, model)
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

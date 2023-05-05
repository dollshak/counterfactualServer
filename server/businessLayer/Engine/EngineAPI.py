import os
import importlib
from abc import abstractmethod
from types import ModuleType

from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.ML_Models.MlModel import MlModel


class EngineAPI:
    def __init__(self, model, file_name, cf_params_list):
        self.model = model
        self.file_name = file_name
        self.cf_params = cf_params_list

    @abstractmethod
    def run_algorithm(self, model_input: list):
        raise Exception("Not implemented.")


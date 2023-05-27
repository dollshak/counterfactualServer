import os
import importlib
from abc import abstractmethod
from types import ModuleType

from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.ML_Models.MlModel import MlModel


class EngineAPI:
    def __init__(self, model, file_name, cf_params_list, config, feature_name_list: list):
        self.model = model
        self.file_name = file_name
        self.cf_params = cf_params_list
        self.config = config
        self.feature_name_list = feature_name_list

    @abstractmethod
    def run_algorithm(self, model_input: list,algo_time_limit):
        raise Exception("Not implemented.")

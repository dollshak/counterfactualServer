import os
import importlib
from abc import abstractmethod
from types import ModuleType

from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.ML_Models.MlModel import MlModel


class EngineAPI:
    def __init__(self):
        pass

    @abstractmethod
    def run_algorithm(self, model: MlModel, algo_name: str, model_input: list, cf_inputs: list):
        raise Exception("Not implemented.")

    @abstractmethod
    def run_algorithms(self, model, inputs: list):
        raise Exception("Not implemented.")

    @abstractmethod
    def import_(self):
        raise Exception("Not implemented.")


    @abstractmethod
    def create_exec(self, name):
        raise Exception("Not implemented.")


    @abstractmethod
    def delete_exec(self, name):
        raise Exception("Not implemented.")


    @abstractmethod
    def run_exec(self, name):
        raise Exception("Not implemented.")


    @abstractmethod
    def run_model(self):
        raise Exception("Not implemented.")
